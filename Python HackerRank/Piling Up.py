#Written by Gskd

for _ in range(int(input())):
    can_stack = True
    size = int(input())
    cubes = [int(i) for i in input().split()]


    for i in range(1, size-1):
        if cubes[i-1] < cubes[i] > cubes[i+1]:
            can_stack = False
            break

    if can_stack:
        print("Yes")
    else:
        print("No")
