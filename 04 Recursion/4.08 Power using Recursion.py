def RecursivePower(n,p):
    if p == 0:
        return 1
    return RecusivePower(n,p-1)*n
