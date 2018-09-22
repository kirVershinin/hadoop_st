import sys

for line in sys.stdin:
    num,usr,ur = line.split()
    if usr == 'user10':
        print('{0}\t{1}\t{2}'.format(num,usr,ur))
