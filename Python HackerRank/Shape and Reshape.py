#Written by Gskd

import numpy

lst = list(map(int, input().strip().split()))

print(numpy.reshape(lst, (3, 3)))
