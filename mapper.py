#!/usr/bin/env python
import sys

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make lower case
    line = line.lower()

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    stopwordsandpunct = set(['the', 'and','i','to','of','you','a',"'",'.',';',',',':','!','?'])

    for word in words:
	if word not in stopwordsandpunct:
           print '%s\t%s' % (word, "1")
