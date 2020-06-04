def equilibrium(arr, n):

  pre = [0 for i in range(n)]
  s = 0
  for i in range(n):
    s += arr[i]
    pre[i] += s

  suff = [0 for i in range(n)]
  s = 0
  for i in range(n-1,-1,-1):
    s += arr[i]
    suff[i] += s

  for i in range(n):
    if pre[i] == suff[i]:
      return i + 1

  return -1

  
arr = [1,3,5,2,2]
print(equilibrium(arr, 5))
