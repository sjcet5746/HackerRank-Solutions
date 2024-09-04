#Written by Gskd
import re
t = int(input())

for i in range(0, t):
    s = input()

    try:
        re.compile(s)
        print(True)
    except re.error:
        print(False)
