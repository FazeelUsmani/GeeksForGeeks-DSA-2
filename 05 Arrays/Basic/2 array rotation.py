def reverse(arr, low, high):
  # low = 0
  # high = len(arr) - 1

  while low<high:
    arr[low], arr[high] = arr[high], arr[low]
    low += 1
    high -= 1

  return arr

def rotate(arr, d):
  n = len(arr)
  reverse(arr,0,d-1)
  reverse(arr,d,n-1)
  reverse(arr,0,n-1)

  return arr

print(rotate([1,2,3,4,5],3))
