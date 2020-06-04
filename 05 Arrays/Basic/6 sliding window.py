def slidingWindow(arr,k):
  n = len(arr)
  sum = 0
  for i in range(k):
    sum += arr[i]
  
  max = sum
  for i in range(k, n):
    sum += (arr[i] - arr[i-k])
    if sum > max:
      max = sum

  return max

print(slidingWindow([1,8,30,-5,20,7],3))
