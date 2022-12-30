def solve(arr: list[int]):
    smallest = min(arr)
    largest = max(arr)
    arr.remove(smallest)
    arr.remove(largest)
    print(sum(arr) + smallest, sum(arr) + largest)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    solve(arr)
