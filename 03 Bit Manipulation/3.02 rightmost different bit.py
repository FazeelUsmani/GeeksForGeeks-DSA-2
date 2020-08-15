def posOfRightMostDiffBit(m,n):
    pos = 1
    if m == 0:
        return int(math.log2(n)+1)
    elif n == 0:
   	return int(math.log2(m)+1)
    else:
        for _ in range(int(math.log2(max(m,n)))):
            a = m & 1
            b = n & 1
            m >>= 1
            n >>= 1
            
            if a != b:
              return pos
            else:
              pos += 1
              
    return pos

# shortcut method: 
def posOfRightMostDiffBit(m,n):
    return int( math.log2((m^n)& -(m^n)) +1 )
