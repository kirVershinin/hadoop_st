import sys

curr_word = None
curr_count = 0

d = {}

class Counter(dict):
    def __missing__(self, key):
        return 0

c = Counter()

for line in sys.stdin:
    count, word = line.split('\t')
    word = word.replace('\n', '')
    count = int(count)
    if word == curr_word:
        curr_count += count
    else:
        if curr_word:
            c[curr_word] += 1
        curr_word = word
        curr_count = count

if curr_word == word:
    c[curr_word] += 1

for i in c:
    print('{0}\t{1}'.format(i,c[i]))
