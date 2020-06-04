# Given an array arr[] of size N where every element is in range from 0 to n-1. Rearrange the given array so that arr[i] becomes arr[arr[i]]. This should be done with O(1) extra space.

# Input Format:
# First line contains an integer denoting the test cases 'T'. First line of each test case contains an integer value depicting size of array 'N' and next line contains N space separated integers denoting the elements of the array.

# Output Format:
# Print all elements of the array after rearranging, each separated by a space, in separate line for each test case.

# User Task:
# The task is to complete the function arrange() which arranges the elements in the array. The printing is done automatically done by the driver code.

# Constraints:
# 1 <= T <= 100
# 1 <= N <= 107
# 0 <= Arr[i] < N

# Example:
# Input:
# 3
# 2
# 1 0
# 5
# 4 0 2 1 3
# 4
# 3 2 0 1

# Output:
# 0 1
# 3 4 2 0 1
# 1 0 3 2

# Explanation:
# Testcase 1: arr[0] = 1 and arr[arr[0]] = 0. Also, arr[1] = 0 and arr[arr[1]] = 1. So, rearranging elements, we get array as, 0 1.

def arrange(arr, n): 
    
    for i in range(n):
        arr[i] += (arr[arr[i]] % n) * n
        
    for i in range(n):
        arr[i] //= n
        
    return arr
