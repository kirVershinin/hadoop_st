import sys

for line in sys.stdin:
    num, words = line.split()
    words = words.split(",")
    i = 0
    for word in words:
            print('{0},{1}\t{2}'.format(num, words[i], 1))
            i += 1
