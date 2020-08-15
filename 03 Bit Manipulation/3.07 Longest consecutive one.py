def maxConsecutiveOnes(x):
    cnt = 0
    while x:
        x = x&(x>>1)
        cnt += 1
    return cnt

print(maxConsecutiveOnes(14))   # Output = 3 as binary(14) = 1110
