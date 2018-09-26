import sys

curr_word = None
curr_count = 0

d = {}

class Counter(dict):
    def __missing__(self, key):
        return 0

c = Counter()

for line in sys.stdin:
    word, count = line.split('\t')
    count = count.replace('\n', '')
    count = int(count)
    if word == curr_word:
        curr_count += count
        c[word] += 1
    else:
        if word:
            c[word] += 1
        curr_word = word
        curr_count = count

for i in c:
    n, nm = i.split('#')
    print('{0}\t{1}\t{2}'.format(n,nm,c[i]))
