long long rev(long long n)
{
    long long rev_num = 0;
     while(n > 0) 
      { 
        rev_num = rev_num*10 + n%10; 
        n = n/10; 
      } 
      return rev_num;
}



long long power(int N,int R);

int main()
{
    int T;
    cin>>T;
    
    while(T--)
    {
        long long N;
        cin>>N;
        
        long long R = 0; 
        
        // reverse the given number n
        R = rev(N);
        long long ans =power(N,R);
        cout << ans<<endl;
    }
}/*This is a function problem.You only need to complete the function given below*/
//You need to complete this fucntion


long long power(int N,int R)
{
//Your code here
if(R==0)
return 1;
return ((power(N,R-1)*N)%(1000000007));

}
