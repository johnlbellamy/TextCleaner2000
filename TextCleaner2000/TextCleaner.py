#!/usr/bin/env python
import re
import pickle
import os
import string

class TextCleaner:
    """
    Takes text where text is an array-like objects and performs:

    alpha_iterator(text) ==>  Returns lower-case letters stripped of 
    punctuation and numbers.
    stop_word_iterator(text) ==>  Removes common "stop" words, like "and".
        Note: By default stop_word_iterator removes numbers. To keep numbers:
        stop_word_oterator(text, remove_numeric = False)
    custom_stop_word_iterator(text, stop_words) ==> Custom stop_words in 
    list format. stop_words are words to be removed.
    can use this in-lieu of stop_word_iterator, or in addition to.
	
    GENERAL USAGE:
        1) If use is for a simple project, with a couple python files, download 
        file to root directory of project, where .py or .ipynb will live.
    Import:
        2) from  TextCleaner2000.TextCleaner import TextCleaner
    Instance Instantiation:
        3a) For simple projects as described in 1), simply  instantiate a 
        cleaner object with empty call: cleaner = TextCleaner()
        3b) For more complicated projects pass the install directory to tell 
        TextCleaner where to locate files and initialize  a cleaner instance:
        WINDOWS: cleaner = TextCleaner("PATH\\TO\\INSTALL\\DIRECTORY\\TextCleaner2000")
        LINUX/UNIX/IOS: cleaner = TextCleaner("PATH/TO/INSTALL/DIRECTORY/TextCleaner2000")
        Call instance methods:
        4) cleaner has instance methods so to use the functions call: 
        cleaner.function_name
    METHOD USAGE:
        For the following examples, text refers to an array-like object. 
        For best results, pass text as a list() or a Pandas 
		 DataFrame column: (assuming data_frame is a pandas DataFrame) data_frame["column_name"].
        For custom stopword removal, pass as a list().	
    GENERAL NUMBER AND PUNCTUATION REMOVAL:
        alpha_words = cleaner.alpha_iterator(text)
    COMMON STOPWORD REMOVAL:
        cleaned_of_stops = cleaner.stop_word_iterator(text)
    CUSTOM STOPWORD REMOVAL:
        cleaned_of_custom_stops = cleaner.custom_stop_word_iterator(text, stop_words)
        Remember that stop_words is a comma-separated list()."""  
    
    def __init__(self, tc_2000_home = ""):
        self.tc_2000_home = tc_2000_home
        pickle_file_path = 'stops.pkl'
        
        if tc_2000_home == "":
            pkl_file = open(os.path.join(os.getcwd() + '\\TextCleaner2000',pickle_file_path), 'rb')
            self.stop_words = pickle.load(pkl_file) 
            pkl_file.close() 
        else:
            pkl_file = open(os.path.join(tc_2000_home,pickle_file_path), 'rb')
            self.stop_words = pickle.load(pkl_file) 
            pkl_file.close() 

    def __alphaizer(self, text, remove_numeric):
        self.text = text
        self.remove_numeric = remove_numeric
        """
        Given a string (text), removes all punctuation and numbers.
        Returns lower-case words. Called by the iterator method
        alpha_iterator to apply this to lists, or array-like (pandas dataframe)
        objects. """
        if remove_numeric:
            result = ''.join(i for i in text if not i.isdigit())
            translation = str.maketrans("","", string.punctuation)
            x = result.translate(translation)
            x = re.sub("^\s" , "" , x) #Removes leading spaces
            x = re.sub("\s+$" ,"" , x) # Removes trailing spaces
            x = re.sub("  "," ", x) #Removes extra spaces
            x = x.replace('\\','').lower()
            return x
        else:
            translation = str.maketrans("","", string.punctuation)
            x = text.translate(translation)
            x = re.sub("^\s" , "" , x) #Removes leading spaces
            x = re.sub("\s+$" ,"" , x) # Removes trailing spaces
            x = re.sub("  "," ", x) #Removes extra spaces
            x = x.replace('\\','').lower() #Removes back-space
            return x
	       
    def __stop_word_remover(self, text, stop):
        """Removes common stop-words like: "and", "or","but", etc. Called by
        stop_word_iterator to apply this to lists, or array-like (pandas dataframe)
        objects. """

        self.text = text
        self.stop = stop
        
        i = 0
        while i < len(stop):
            text = re.sub("\s"+stop[i]+"\s|^"+stop[i]+"\s|\s"+stop[i]+"$", " ", text)
            i += 1
        
        return text
    
    def __word_remover(self, text, stop):
        """Removes custom stop-words. For example, "patient", or "medicine", if
        one is dealing with medical text. Can use this method to pass any set of stop
        words, or in-lieu of common stop-word method stop_word_iterator. Called by
        word_iterator to apply this to lists, or array-like (pandas dataframe)
        objects. """
    
        self.text = text
        self.stop = stop
     
        i = 0
        while i < len(stop):
            text = re.sub("\s"+stop[i]+"\s|^"+stop[i]+"\s|\s"+stop[i]+"$", " ", text)
            text = re.sub("  "," ", text) #Removes extra spaces
            text = re.sub("^\s" , "" , text) #Removes leading spaces
            text = re.sub("\s+$" ,"" , text) # Removes trailing spaces
            i += 1
        
        return text
    
    def stop_word_iterator(self, text):
        """Calls __stop_word_remover to apply this method to array-like objects.
        Usage: TextCleaner.stop_word_iterator(text)."""

        self.text = text
        
        text2 = [self.__stop_word_remover(x,self.stop_words) for x in text]
        
        return text2
    
    def alpha_iterator(self, text, remove_numeric = True):
        """
        Calls __alphaizer to apply this method to array-like objects. Usage:
        TextCleaner.alphaizer(text).
        Note: By default this method removes numbers from each string.
        To change this behavior pass the flag remove_numerals:
        alphaizer(text, remove_numerals = False)
        """
        self.text = text
        self.remove_numeric = remove_numeric
        text2 = [self.__alphaizer(x, remove_numeric) for x in text]
        
        return text2
    
    def custom_stop_word_iterator(self, text, stop_words):
        """Removes custom stop-words. For example, "patient", or "medicine", if
        one is dealing with medical text and do not want to include those words 
        in analysis. Can use this method to pass any set of stop
        words, or in-lieu of common stop-word method stop_word_iterator.Calls 
        __word_remover to apply this method to array-like objects. Usage:
        TextCleaner.custom_stop_word_iterator(text, stop_words), where 
        stop-words and text are in a comma-
        separated list, or iterable."""

        self.text = text
        
        text2 = [self.__word_remover(x,stop_words) for x in text]
        
        return text2
    

        