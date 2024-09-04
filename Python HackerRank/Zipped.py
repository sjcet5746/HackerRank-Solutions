#Written by Gskd
n = list(map(int, input().split()))
lista = []

for i in range(n[1]):
    lista.append(list(map(float, input().split())))
X = list(zip(*lista))

for j in X:
    print(sum(j)/n[1])
