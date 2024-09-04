#Written by Gskd
from collections import Counter
a=Counter(input())
q=[]
for i in range(len(a)):q.append(0)
for i in sorted(a.items()):
    for m in range(len(list(reversed(sorted(a.values()))))):
        if i[1]==list(reversed(sorted(a.values())))[m] and q[m]==0:
            q[m]=i[0]
            break
for i in range(3):print(q[i],list(reversed(sorted(a.values())))[i])
