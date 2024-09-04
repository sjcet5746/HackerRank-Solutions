#Written by Gskd

import numpy

order = int(input())
Array = numpy.array([input().split() for i in range(order)], float)
Array.shape = (order, order)
print(round(numpy.linalg.det(Array), 2))
