def josephus(n,k):
    if n == 1:
        return n
    return (josephus(n-1,k)+k-1)%n+1
