#Written by Gskd

import numpy as np

axis0, axis1 = input().split()
data = []
for row in range(int(axis0)):
    data.append([int(column) for column in input().split()])

np_arr = np.array(data)

print(np.max(np.min(np_arr, 1)))
