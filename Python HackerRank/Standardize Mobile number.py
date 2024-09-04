
#Written by Gskd
from re import sub

def wrapper(f):
    r = r"^(?:\+?91|0)??(\d{5})(\d{5})$"
    s = r"+91 \1 \2"

    def fun(li):
        return f([sub(r, s, i) for i in li])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
