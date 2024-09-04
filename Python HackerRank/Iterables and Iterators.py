#Written by Gskd
from itertools import combinations, groupby

count, letters, to_select = int(input()), input().split(), int(input())

letters = sorted(letters)

combinations_of_letters = list(combinations(letters, to_select))

contain = len([c for c in combinations_of_letters if 'a' in c])

print(contain / len(combinations_of_letters))
