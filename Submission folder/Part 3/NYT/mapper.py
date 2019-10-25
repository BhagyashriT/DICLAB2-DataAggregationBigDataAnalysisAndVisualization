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
        if len(word) > 3 and len(word) < 15 and 'class' not in word and 'href' not in word and 'body' not in word and \
                'block' not in word and 'home' not in word and 'pp' not in word and 'wasp' not in word and 'style' not \
                in word and 'label' not in word and 'default' not in word and 'span' not in word:
            clean_word_list.append(word)

    for word in clean_word_list: print '%s\t%s' % (word, 1)


stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
              'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such',
              'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from',
              'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through',
              'don', 'nor', 'me', 'were', 'her', 'more', 'himself', 'this', 'down', 'should', 'our', 'their',
              'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any',
              'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then',
              'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you',
              'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
              'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further',
              'was', 'here', 'than', 'it\'s', 'labeldefault', 'from', 'like', 'visiblelgblock',
              'visiblemdblock', 'said', 'would', 'also', 'advertisement', 'time','show', 'gets', 'first','said','people'
                ,'could', 'years','last','even','year','many','times','back','ever','away','role','told','come','every'
              'often','found','real','here','whether','last','work', 'take', 'well', 'little', 'didn\'t', 'public', 'came',
              'early','started','look','think','made','many','kind','york','play','percent','start','part','less','makes'
              'help','past','since','called','city','wrote','great','woman','that\'s','times','it\'s','people','going',
              'including','read','things','years','house','week','making','executive', 'amazon','enough','trying','much',
              'make','through','there\'s','close','face','even','something','woman','whose','life','really','back','around'
              'three','time','later','still','said','might','know','long','next','find','became','former','that','night'
              'different','second','trump','president','make','want','thing']

for line in sys.stdin:
    word_list = []
    line = line.strip()
    line = line.lower()
    words = line.split()

    for wod in words:
        if wod not in stop_words:
            word_list.append(wod)
    clean_up_list(word_list)