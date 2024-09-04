#Written by Gskd
n = int(input())
n_ = set(map(int, input().split()))

b = int(input())
b_ = set(map(int, input().split()))

p = n_.symmetric_difference(b_)

length = len(p)

print(length)
