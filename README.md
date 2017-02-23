# WordCleaner2000
A light-weight stop-word/custom stop-word removal tool and text cleaner.

You can put this in your python-dev directory or put it in your working directory. You need to pass the working directory as part of the initialization. See below for sample usage.

from  WordCleaner2000.WordCleaner import WordCleaner

#Pass install directory as first argument
cleaner = WordCleaner("/install/directory/WordCleaner2000")

clean_text = cleaner.alpha_iterator(pd.DataFrame['Column'] or list)

clean_text2 = cleaner.stop_word_iterator(pd.DataFrame['Column'] or list)

#Perhaps the best feature is the ability to pass a list to remove custom stop words.

custom_stop_words =["custom_stopword1","custom_stopword2","custom_stopwordn"]

clean_text3 = cleaner.word_iterator(pd.DataFrame['Column'] or list, custom_stop_words)
