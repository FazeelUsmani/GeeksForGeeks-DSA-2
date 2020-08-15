
def possibleWords(arr, n, output = ""):
    if len(arr) == 0:
      print(output, end = " ")
      return
    
    text = getString(arr[0])
    for i in text:
      possibleWords(arr[1:], n, output+i)
      
      
def getString(d):
    if d == 2:
        return "abc"
    if d == 3:
        return "def"
    if d == 4:
        return "ghi"
    if d == 5:
        return "jkl"
    if d == 6:
        return "mno"
    if d == 7:
        return "pqrs"
    if d == 8:
        return "tuv"
    if d == 9:
        return "wxyz"
    return ""


    
    ##Your code here
