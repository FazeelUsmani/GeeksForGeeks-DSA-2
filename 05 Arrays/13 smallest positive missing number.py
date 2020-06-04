def missingNumber(arr,n):
    
    max1 = max(arr)
    if max1 < 1:
        return 1
        
    if n == 1:
        return 2 if arr[0] == 1 else 1
    
    l = [0]*max1
    for i in range(n):
        if arr[i] > 0:
            if l[ arr[i]-1 ] != 1:
                l[arr[i]-1] = 1
                
    for i in range(len(l)):
        if l[i] == 0:
            return i + 1
    return i + 2
    
