import sys
import json
data = []
with open('stores.json', 'r') as f:
    data = json.load(f)

maxlen = 0
maxsize = 0

for draw in data:

    first = draw['first']
    second = draw['second']

    for i in first:
        maxlen = max(len(i[-1]), maxlen)
        maxsize = max(maxsize, sys.getsizeof(i[-1]))

    for i in second:
        maxlen = max(len(i[-1]), maxlen)
        maxsize = max(maxsize, sys.getsizeof(i[-1]))

print(maxlen, maxsize)
