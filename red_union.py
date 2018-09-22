import sys

curr_count = None

for line in sys.stdin:
    count, word = line.split('\t')
    if count == curr_count:
        pass
    else:
        if curr_count:
            print('{0}'.format(curr_count))
        curr_count = count

if curr_count == count:
    print('{0}'.format(curr_count))
