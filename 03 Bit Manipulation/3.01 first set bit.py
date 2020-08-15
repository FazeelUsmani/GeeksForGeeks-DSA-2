# Logic: Calculating 2's complement and using Bitwise AND 

# For Example, n = 20

# In binary,        20 = 10100
# 2's complement of 20 = 1's complement + 1

# 1's complement of 20 = Toggling all bits (I mean 1 to 0 and 0 to 1)
# 1's complement of 20 = 01011

# Adding 1 to 1's complement of 20 = 01011 (11)
#                                    +   1 (+1) 
# So, 2's complement of 20 is        01100 (12)        

# Now, do a bitwise & with n
#     10100 (20)
#   & 01100 (12)
# res 00100 (8)

# log(8) will return 2 as the set bit postion is 2

# Add 1 to it = 2+1 = 3

import math

for x in range(int(input())):
    n = int(input())
    if n == 0:
        print(0)
    else:
        print(int(math.log2(n&-n)+1))

        
        
# Aliter: (Another approach - Naive):

def getFirstSetBit(n):
    flag = True
    c = 1
    
    while n:
      if n & 1:
        return c
      c += 1
      n = n >> 1
    return 0
        

# Remember the following while doing Bit Manipulation problems:

# log2(n & -n)+1 - > returns the position of the rightmost set bit
# log2(n)+1 -> returns the number of digits in the binary representation of the given number
# log10(n)+1 -> returns the number of digits in the number decimal number O(1) time
# x=x&(x-1) -> turn off the rightmost set bit
# 1<<n --=""> 1*(2^n) and all the term will be zero except the one
