# Division rule:

# Here, We will use the formula Dividend = Divisor * Quotient + Remainder
# where Divisor = size of array
#           Quotient = New number at index i after rearrangement
#           Remainder = Old Number at index i before rearrangement
#           Dividend = The number stored at index i
# While Traversing the array, we will Look for the value at arr[arr[i]] (which is to be stored at index i), multiply it with Divisor (size of array), and add the old value present at arr[i] to it.
# Dvisor is a value which is higher then values in array (in this case n - size of array, as array elements are between 0 to n-1)

# Obviously, don't forget to remove the multiplier n from the values while accessing and outputting the new values.


def div(arr,n):
  maxi = n-1
  mini = 0
  
  me = arr[n-1] + 1
  for i in range(n):
    if i & 1:
      arr[i] += (arr[mini]%me)*me
      mini += 1

    else:
      arr[i] += (arr[maxi]%me)*me
      maxi -= 1
    
  
  for i in range(n):
    arr[i] //= me
  
  
  return arr


# Given a sorted array of positive integers. Your task is to rearrange  the array elements alternatively i.e first element should be max value, second should be min value, third should be second max, fourth should be second min and so on...

# Note: O(1) extra space is allowed. Also, try to modify the input array as required.

# Input:
# First line of input conatins number of test cases T. First line of test case contain an integer denoting the array size N and second line of test case contain N space separated integers denoting the array elements.

# Output:
# Output the modified array with alternated elements.

# Constraints:
# 1 <=T<= 100
# 1 <=N<= 107
# 1 <=arr[i]<= 107

# Example:
# Input:
# 2
# 6
# 1 2 3 4 5 6
# 11 
# 10 20 30 40 50 60 70 80 90 100 110

# Output:
# 6 1 5 2 4 3
# 110 10 100 20 90 30 80 40 70 50 60

# Explanation:
# Testcase 1: Max element = 6, min = 1, second max = 5, second min = 2, and so on... Modified array is : 6 1 5 2 4 3.
