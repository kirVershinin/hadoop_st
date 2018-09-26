import sys
import re

for line in sys.stdin:
    p = re.compile(r'\W+')
    line = p.split(line)
    line = line[:-1]
    nm = line[0]
    l = line[1:]
    for word in l:
        print ('{0}#{1}\t{2}'.format(word,nm, 1))
