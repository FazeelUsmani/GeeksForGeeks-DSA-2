# Logic:
# Find local minima and local maxima:

def stockBuy(arr):
  n = len(arr)
  if n == 1:
    return arr[0]

  tot = 0
  i = 1
  temp = arr[0]
  while i < n-1:
    if arr[i+1] <= arr[i]:
      tot += (arr[i] - temp)
      temp = arr[i+1]
      i += 1
    i += 1

  tot += arr[n-1] - temp    
  if tot < 0:
    return 0
  else:
    return tot


print(stockBuy([1,5,3,8,12]))
print(stockBuy([10,5,3]))
print(stockBuy([1,2,5]))
