#Written by Gskd
import numpy as np
n, _ = map(int, input().split())
a = np.array(list(input().split() for _ in range(n)), int)
b = np.array(list(input().split() for _ in range(n)), int)
print(a + b, a - b, a * b, a // b, a % b, a ** b, sep='\n')
