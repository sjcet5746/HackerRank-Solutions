#Written by Gskd
def print_sorted(table: list, sort_column: int) -> None:
    table.sort(lambda x: x[sort_column])
    for row in table:
        print(*row)


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    print_sorted(arr, k)
