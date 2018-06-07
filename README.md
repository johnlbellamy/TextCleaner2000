# TextCleaner2000
A light-weight stop-word/custom stop-word removal tool and text cleaner.

You can put this in your python-dev directory or put it in your working directory. You need to pass the working directory as part of the initialization. See below for sample usage.

# Add to first line of Jupyter or where your imports go:

from  TextCleaner2000.TextCleaner import TextCleaner

# For Help and detailed usage:
help(cleaner)

# Pass install directory as first argument

UNIX-LIKE:
cleaner = TextCleaner("install/location/WordCleaner2000")

WINDOWS:
cleaner = TextCleaner("install\\location\\WordCleaner2000")

# To remove numbers and punctuation/symbols:
text_without_numbers_or_symbols = cleaner.alpha_iterator(pd.DataFrame['Column'] or list)

# To remove commons top words like "and","or", "the", etc.:
text_with_common_stops_removed = cleaner.stop_word_iterator(pd.DataFrame['Column'] or list)

# Perhaps the best feature is the ability to pass a list to remove custom stop words.

custom_stop_words =["custom_stopword1","custom_stopword2","custom_stopwordn"]

text_with_custom_stops_removed  = cleaner.custom_stop_word_iterator(pd.DataFrame['Column'] or list, custom_stop_words)
