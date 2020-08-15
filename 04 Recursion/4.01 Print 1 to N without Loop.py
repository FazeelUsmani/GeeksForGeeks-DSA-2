n = int(input())

def num(n):
  if n == 0:
    return 
  num(n-1)
  print(n, end = " ")  

num(n)
