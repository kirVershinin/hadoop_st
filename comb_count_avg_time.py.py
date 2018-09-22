import sys

d = {}
   
class Counter(dict):
    def __missing__(self, key):
        return 0

c = Counter()

for line in sys.stdin:
    words = line.split()

    for word in words:
        c[word] += 1
    
for i in c:
    print ('{0}\t{1}'.format(i, c[i]))
