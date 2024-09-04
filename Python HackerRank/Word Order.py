#Written by Gskd
from collections import Counter
N = int(input())
M = []
set1= set()
count = 0
for i in range(N):
    str1= input()
    M.append(str1)
x = Counter(M)
for i in M:
    if i not in set1:
        set1.add(i)
        count+=1
    else:
        continue
print(count)
for i in x.values():
  print(i, end = " ")
