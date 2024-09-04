#Written by Gskd

import numpy as np

def task(arr):
        np_array = np.array(arr)
        mean_array = np.mean(np_array, axis=1)
        var_array = np.var(np_array, axis=0)
        std_array = np.std(np_array)
        return [mean_array, var_array, round(std_array, 11)]

if __name__ == '__main__':
        arr = []
        n, m = list(map(int, input().split()))
        for i in range(n):
                arr.append(list(map(int, input().split())))
        result = task(arr)
        print(*result, sep="\n")
