import sys
  
curr_word = None
curr_count = 0

d = {}

class Counter(dict):
    def __missing__(self, key):
        return 0

c = Counter()

nl = []

for line in sys.stdin:
    nl.append(line.replace('\t',',').replace('\n','').replace(';',','))
    word, st = line.split('\t')
    n,tf,cn = st.split(';')
    count = int(cn)
    if word == curr_word:
        curr_count += count
        c[word] += 1
    else:
        if word:
            c[word] += 1
        curr_word = word
        curr_count = count

i = 0
for x in nl:
    nl[i] = x.split(',')
    if nl[i][0] in c.keys():
        nl[i][3] = c[nl[i][0]]
    i += 1

for x in nl:
    print('{0}#{1}\t{2}\t{3}'.format(x[0],x[1],x[2],x[3]))




























