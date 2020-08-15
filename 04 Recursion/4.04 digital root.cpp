int digitalRoot(int n)
{
    if (n <10)
    return n;
    
    return digitalRoot(n%10 + n/10);
    
}
