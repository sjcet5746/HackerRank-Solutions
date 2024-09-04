#Written by Gskd
from itertools import combinations_with_replacement
a, b = input().split()
a = sorted(a)
x = list(combinations_with_replacement(a, int(b)))
[print(''.join(j)) for j in x]
