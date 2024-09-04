#Written by Gskd
import numpy as np
n,m=map(int,input().split())
arr = []

for _ in range(n):
    row=list(map(int,input().split()))
    arr.append(row)

arr=np.array(arr)
print(np.transpose(arr))
print(arr.flatten())
