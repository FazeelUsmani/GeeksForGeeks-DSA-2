def solve(arr,n):
  s = []
  flag = False
  for i in range(n):
    if not flag:
      if i != n-1 and arr[i] < arr[i+1]:
        s.append(i)
        flag = True

    if flag:
      if i == n-1 or arr[i] > arr[i+1]:
        s.append(i)
        flag = False

  return s
  
  
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    res = solve(arr,n)
    for i in range(0,len(res),2):
        print("(",res[i],res[i+1],")", end = " ")
    print()
    
 
