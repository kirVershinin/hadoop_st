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
    if 'A' in d[i]  and 'B' in d[i]:
        pass
    else:
        print(i)
