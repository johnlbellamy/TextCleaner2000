# TextCleaner2000
A light-weight stop-word/custom stop-word removal tool and text cleaner.

# Install
1) Download or clone File
2) Unzip file. You can put unzipped file in your python-dev directory or put it in your project's working directory. 
   For smaller projects, where a few files "live" in the same root as TextCleaner2000, simply place 
   TextCleaner2000/TextCleaner2000 in your project's root direcory.
   
   For larger projects, or to specify a specific directory you can pass the chosen TextCleaner2000 directory as the only 
   argument in object instantiation. See below for sample usage.

# Add to first line of Jupyter or where your imports go:

from  TextCleaner2000.TextCleaner import TextCleaner

# For Help and detailed usage:
help(cleaner)

#Usage
# Instantiate Cleaner Object:
## By placing TextCleaner2000 in root directory of project:

cleaner = TextCleaner()

## Specify install directory; Pass install directory as first argument

UNIX-LIKE:
cleaner = TextCleaner("install/location/TextCleaner2000")

WINDOWS:
cleaner = TextCleaner("install\\\location\\\TextCleaner2000")

# To remove numbers and punctuation/symbols:
## text is pd.DataFrame['Column'] or list (array-like) object.

text_without_numbers_or_symbols = cleaner.alpha_iterator(text)

## By default, alpha_iterator removes numbers as well. To change this and keep numbers:
text_without_symbols = cleaner.alpha_iterator(text, remove_numeric = False)

# To remove common stop words like "and","or", "the", etc.:
text_with_common_stops_removed = cleaner.stop_word_iterator(text)

# Perhaps the best feature is the ability to pass a list to remove custom stop words.

custom_stop_words =["custom_stopword1","custom_stopword2","custom_stopwordn"]

text_with_custom_stops_removed  = cleaner.custom_stop_word_iterator(text, custom_stop_words)
