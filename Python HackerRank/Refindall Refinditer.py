#Written by Gskd

import re

if __name__=="__main__":
    s = input()
    r = re.findall(r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])',s)
    if not r:
        print(-1)
    else:
        for p in r:
            print(p)
