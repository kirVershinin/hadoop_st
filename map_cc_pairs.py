import sys

for line in sys.stdin:
    words = line.split()
    for i in words:
        for j in words:
            if i != j:
                print('{0},{1}\t{2}'.format(i,j,1))
