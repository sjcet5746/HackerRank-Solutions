#Written by Gskd

n = int(input())
s = list(map(int, input().split()))
s = set(s[::-1])
c = int(input())
for i in range(c):
    l = input().split()

    if l[0] == 'pop':
        try:
            s.pop()
        except:
            None
    elif l[0] == 'remove':
        try:
            s.remove(int(l[1]))
        except:
            None
    else:
       s.discard(int(l[1]))

print(sum(s))
