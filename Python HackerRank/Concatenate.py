#Written by Gskd
import numpy

n, m, p = map(int, input().split())
lst1 = []
lst2 = []

for i in range(n):
    lst1.append([*map(int, input().split())])
arr1 = numpy.array(lst1)

for i in range(m):
    lst2.append([*map(int, input().split())])
arr2 = numpy.array(lst2)

print(numpy.concatenate((arr1, arr2), axis=0))
