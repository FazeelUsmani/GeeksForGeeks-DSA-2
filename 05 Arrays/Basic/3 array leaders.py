arr = [5,3,20,15,8,3]
n = len(arr)
max = -999999
for i in range(n-1,-1,-1):
  if arr[i] > max:
    print(arr[i], end = " ")        # you can use stack and then print to get in the same order
    max = arr[i]

# Leader of an array are the elements in which no element on the right side of teh element is greater than that number 

