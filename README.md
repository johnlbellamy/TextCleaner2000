# TextCleaner2000
A light-weight stop-word/custom stop-word removal tool and text cleaner.

# Install
1) Download or clone File
2) Unzip file. You can put unzipped file in your python-dev directory or put it in your project's working directory. 
   For smaller projects, where a few files "live" in the same root as TextCleaner2000, simply place 
   TextCleaner2000/TextCleaner2000 in your project's root direcory.
   
   For larger projects, or to specify a specific directory you can pass the chosen TextCleaner2000 directory as the only 
   argument in object instantiation. See below for sample usage.

# Add to imports:

from  TextCleaner2000.TextCleaner import TextCleaner

# For Help and detailed usage:
help(cleaner)

# Usage
## Instantiate Cleaner Object:
## Place (copy and paste) folder TextCleaner2000\TextCleaner20000 in root directory of project:
### Then:
cleaner = TextCleaner()

# To remove numbers and punctuation/symbols:
## text is pd.DataFrame['Column'] or list (array-like) object.

text_without_numbers_or_symbols = cleaner.alpha_iterator(text)

## By default, alpha_iterator removes numbers as well. To change this and keep numbers:
text_with_numbers = cleaner.alpha_iterator(text, remove_numeric = False)

## By default, alpha_iterator removes all puntuation obviously including emoticons. To change this and keep emoticons:
text_with_emoticons = cleaner.alpha_iterator(text, remove_emoticon = False)

## You can remove emoticons and numbers, keep both, or keep one and not the other by passing both flags:
text_with_emoticons_and_numbers = cleaner.alpha_iterator(text, remove_numeric = False, remove_emoticon = False)

# To remove common stop words like "and","or", "the", etc.:
text_with_common_stops_removed = cleaner.stop_word_iterator(text)

# Perhaps the best feature is the ability to pass a list to remove custom stop words.

custom_stop_words =["custom_stopword1","custom_stopword2","custom_stopwordn"]

text_with_custom_stops_removed  = cleaner.custom_stop_word_iterator(text, custom_stop_words)
