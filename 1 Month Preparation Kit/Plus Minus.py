def solve(arr):
    pcount = 0
    ncount = 0
    zeroes = 0
    
    for val in arr:
        if val > 0:
            pcount += 1
        elif val < 0:
            ncount += 1
        else:
            zeroes += 1

    return pcount, ncount, zeroes


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    a, b, c = solve(arr)

    print(round(a/n, 6))
    print(round(b/n, 6))
    print(round(c/n, 6))
