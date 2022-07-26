n, k = map(int, input().split())


def combination(n: int, k: int):
    if k == 0:
        return 1
    elif k > n:
        return 0
    else:
        return combination(n - 1, k) + combination(n - 1, k - 1)


res = combination(n, k)

print(res)
