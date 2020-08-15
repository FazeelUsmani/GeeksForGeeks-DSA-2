# kth set bit
x = 14
k = 2

# Logic: right shifting k elements and 
# checking the kth bit is set or not 

if (x >> k) & 1:
  print("True")
  
else:
  print("False")

