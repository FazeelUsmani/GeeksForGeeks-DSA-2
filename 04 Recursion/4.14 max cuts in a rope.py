def maxCuts(n,a,b,c):
  if n == 0:
    return 0
  
  if n < 0:
    return -1
    
  res = max(maxCuts(n-a,a,b,c),
        maxCuts(n-b,a,b,c),
        maxCuts(n-c,a,b,c))

  if res == -1:
    return -1

  return res+1

print(maxCuts(23,11,9,12))
