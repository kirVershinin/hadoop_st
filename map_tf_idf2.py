import sys

for line in sys.stdin:
    w,g,n = line.split('\t')
    n = n.replace('\n', '')
    print ('{0}\t{1};{2};1'.format(w,g,n))

