def solve(n):
    flipped_bits = ""
    bits = bin(n)[2:]

    if len(bits) < 32:
        bits = "0" * (32 - len(bits)) + bits

    for bit in bits:
        if int(bit) == 1:
            flipped_bits += "0"
        else:
            flipped_bits += "1"
    return flipped_bits


if __name__ == '__main__':
    q = int(input().strip())

    for _ in range(q):
        n = int(input().strip())
        res = solve(n)
        print(int(res, 2))
