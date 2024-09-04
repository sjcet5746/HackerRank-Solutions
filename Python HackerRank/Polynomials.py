#Written by Gskd

import numpy as np

if __name__=="__main__":
    p = np.array(input().split(), float)
    x = int(input())
    print(np.polyval(p, x))
