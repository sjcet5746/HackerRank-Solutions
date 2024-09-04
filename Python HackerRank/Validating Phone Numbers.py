#Written by Gskd
n= int(input())

for i in range(n):
    mob = str(input())
    if mob.isnumeric() == True and mob[0:1] in ['7','8','9'] and len(mob) == 10 :
        print('YES')
    else:
        print('NO')
