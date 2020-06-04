# Fibonacci means 2, N-Bonacci means n elements sum

# N-bonacci:

def nBonacci(n,m):
  arr = [0 for i in range(m)]
  arr[n-1] = 1
  sum = 0
  for i in range(n,m):
    sum += arr[i-1]
    arr[i] = sum
    sum -= arr[i-n]

  return arr

print(nBonacci(4,10))
