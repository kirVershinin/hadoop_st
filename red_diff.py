import sys

d = {}

for line in sys.stdin:
    count, word = line.split('\t')
    word = word.replace('\n','')

    if count in d:
        d[count].append(word)
    else:
        d[count] = [word]

for i in d:
    if 'B' not in d[i]:
        print (i)
