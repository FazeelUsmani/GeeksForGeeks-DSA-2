# This solution works only for non-negative integers. If there are negative integers in the array then you need to use Hashing

def subArrayWithGivenSum(arr,sum):
  n = len(arr)
  tot = 0
  index = 0
  for i in range(n):    
    while tot > sum:
      tot -= arr[index]
      index += 1
    if tot == sum:
      return True
    elif tot < sum:
      tot += arr[i]
    
  return False

print(subArrayWithGivenSum([1,4,20,3,10,5],33))
print(subArrayWithGivenSum([1,4,0,0,3,10,5],17))
print(subArrayWithGivenSum([2,4], 3))
