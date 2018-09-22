import sys


for line in sys.stdin:
    words = line.split()
    for i in words:
        class Counter(dict):
            def __missing__(self, key):
                return 0

        c = Counter()
        for j in words:
            if i != j:
                c[j] += 1
        res = ",".join(("{}:{}".format(*i) for i in c.items()))        
        print('{0}\t{1}'.format(i,res))
