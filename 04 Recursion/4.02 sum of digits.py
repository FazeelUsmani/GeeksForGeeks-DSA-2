def sumOfDigits(n):
    if n == 0:
        return 0
    sum = n%10
    n //= 10
    return sum + sumOfDigits(n)
