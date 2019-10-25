#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import collections

current_word = None
current_count = 0
word = None
counter = collections.Counter()
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    counter[word] += count
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
            # write result to STDOUT
            # Counter(current_word).most_common(10)
            
        current_count = count
        current_word = word

# do not forget to output the last word if needed!

topTen = counter.most_common(10)
for item in topTen:
    print(item[0]+","+str(item[1])) 