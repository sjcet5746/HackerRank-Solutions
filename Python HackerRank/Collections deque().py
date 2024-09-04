#Written by Gskd
from collections import deque
d = deque()
n = int(input())
for i in range(n):
    a = list(input().split())
    if a[0] == 'append':
        d.append(a[1])
    elif a[0] == 'appendleft':
        d.appendleft(a[1])
    elif a[0] == 'pop':
        d.pop()
    else:
        d.popleft()
print(' '.join(d))
