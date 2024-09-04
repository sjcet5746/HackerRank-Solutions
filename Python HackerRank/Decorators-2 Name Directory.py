#Written by Gskd
import operator

def to_int(fun):
    def inner(*args, **kwargs):
        return int(fun(*args, **kwargs))
    return inner

def person_lister(f):
    def inner(people):
        people.sort(key=to_int(operator.itemgetter(2)))
        return (f(person) for person in people)
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
