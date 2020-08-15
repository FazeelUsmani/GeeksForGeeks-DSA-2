def countSetBits(n):
    cnt = 0
    for i in range(1,n+1):
        t = i
        while t > 0:
            cnt += 1
            t = t & (t-1)
            
    return cnt
