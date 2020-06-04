def trap(arr):
  n = len(arr)
  leftMax, rightMax = [0 for i in range(n)],[0 for i in range(n)]
  max1 = 0
  for i in range(0,n):
    if arr[i] > max1:
      max1 = arr[i]
    leftMax[i] = max1

  max2 = 0
  for j in range(n-1,-1,-1):
    if arr[j] > max2:
      max2 = arr[j]
    rightMax[j] = max2

  out = []
  for i in range(n):
    out.append(min(leftMax[i], rightMax[i]) - arr[i])

  #print(leftMax, rightMax)  
  print(" Total rain water trapped = ",out)


trap([3,0,1,2,5])
