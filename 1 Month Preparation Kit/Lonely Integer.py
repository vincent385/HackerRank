def solve(n: int, arr: list[int]):
    occurence_dict = {}
    for i in range(n):
        if occurence_dict.get(str(arr[i])):
            occurence_dict[str(arr[i])] += 1
        else:
            occurence_dict[str(arr[i])] = 1

    for key, value in occurence_dict.items():
        if value == 1:
            print(key)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    solve(n, arr)
