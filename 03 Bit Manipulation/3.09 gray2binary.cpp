int grayToBinary(int num)
{    
    int n = num;
    
    while (n >= 1){
        n>>=1;
        num = num^n;
    }
    
    return num;
}