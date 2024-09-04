#Written by Gskd
if name == 'main':
    n = int(input())
    integerList = map(int, input().split())
    t = tuple(integerList)
    myhash = hash(t)
    print(myhash)
