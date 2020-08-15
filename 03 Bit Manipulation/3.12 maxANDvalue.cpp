// Checking if there are >1 number following the pattern
bool checkBit(int pattern, int arr[], int n){
    int cnt = 0;
    for (int i = 0; i < n; ++i){
        if ((arr[i]&pattern) == pattern){
            cnt++;
        }
    }
    return (cnt>1)?1:0;
}

 
// Function for finding maximum and value pair
int maxAND (int arr[], int n)
{
    if (n == 1)
        return 0;
    
    int res = 0;
    bool ans;
    for (int bit = 31; bit >= 0; --bit){
        ans = checkBit(res|(1<<bit), arr, n);
        if (ans == true)
            res |= (1<<bit);
    }
    return res;
}
