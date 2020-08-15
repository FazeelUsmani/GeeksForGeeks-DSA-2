def permute(a, l, r):
    if l == r:
        arr.append(toString(a))

    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]

    return arr


for t in range(int(input())):
    string = input()
    n = len(string)
    a = list(string)
    arr = []
    x = permute(a, 0, n - 1)
    x.sort()
    print(*x)
