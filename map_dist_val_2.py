import sys

for line in sys.stdin:
    words = line.split(',')
    words = words[1:]
    for word in words:
        #word = word.replace('\n','')
        print ('{0}\t{1}'.format(word[:-1], 1))

