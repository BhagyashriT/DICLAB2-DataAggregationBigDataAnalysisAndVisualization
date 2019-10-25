#!/usr/bin/env python
"""mapper.py"""
import sys


# input comes from STDIN (standard input)
def clean_up_list(word_list):
    clean_word_list = []

    for word in word_list:
        symbols = "\'!@#$%^&*()+_{<>}:\"<>?.,;[]-=1234567890"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
        if len(word) > 3 and len(word) < 15 and 'class' not in word and 'href' not in word and 'body' not in word and 'data' not in word:
            clean_word_list.append(word)
      
    for word in clean_word_list: print '%s\t%s' % (word, 1)

stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
              'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such',
              'into', 'of', 'most', 'itself', 'other', 'off', ' is ', 's', 'am', ' or ', 'who', 'as', 'from ',
              'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their',
              'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any',
              'before', 'them', 'same', ' and ', 'been', 'have', ' in ', 'will', 'on', 'does', 'yourselves', 'then',
              'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', ' not ', 'now', 'under', 'he', 'you',
              'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
              'whom', 't', 'being', ' if ', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further',
              'was', 'here', 'than','it\'s']
    
for line in sys.stdin:
    word_list = []
    line = line.strip()
    line = line.lower()
    words = line.split()

    for wod in words:
        if wod not in stop_words:
            word_list.append(wod)
    clean_up_list(word_list)