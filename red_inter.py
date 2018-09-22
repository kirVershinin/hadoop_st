import sys

curr_word = None
curr_count = 0

d = {}

for line in sys.stdin:
    count, word = line.split('\t')
    word = word.replace('\n','')
    
    if count in d:
        d[count].append(word)
    else:
        d[count] = [word]

for i in d:
    if len(d[i]) >= 2:
        print (i)

