def countBitsFlip(a,b):
    x = a ^ b
    cnt = 0
    while (x):
        x = x & (x-1)
        cnt += 1
        
    return cnt
