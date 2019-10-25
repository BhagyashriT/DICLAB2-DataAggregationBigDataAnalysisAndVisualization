#!/usr/bin/env python

import sys
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
              'different','second','ha','re','wa']
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    line = line.lower()
    for i in "\'`!@#$%^&*()+_{<>}:\"<>?.,;[]-=1234567890":
        line = line.replace(i, "")
    #word_list = []
    #clean_word_list = []
    # split the line into words
    words = line.split()
    #TW1
    tops = set(["watch","star","marvel","wars","thrones","game","movies","like","disney","drama"])
    #CC2
    #tops = set(["marvel","season","marvels","punisher","trailer","fantastic","four","spiderman","earths","mightiest"])
    #NYT3
    #tops = ["film","movie","story","company","world","season","best","book","series","black"]
    #for wod in words:
    #    if wod not in stop_words:
    #        word_list.append(wod)
    # for word in word_list:
    #     symbols = "\'!@#$%^&*()+_{<>}:\"<>?.,;[]-=1234567890"
    #     for i in range(0, len(symbols)):
    #         word = word.replace(symbols[i], "")
    #     if len(word) > 3:
    #         words.append(word)
    for i in range(len(words) - 1):
        for j in range(i + 1, len(words)):
            if (words[i] != words[j]) and (words[i] in tops) and (words[j] not in stop_words):
                if words[i] < words[j]:
                    word1 = words[i]
                    word2 = words[j]
                else:
                    word2 = words[i]
                    word1 = words[j]
                print ("%s|%s\t%s" % (word1, word2, 1))