vector<int> leaders(int arr[], int n){
    vector<int> v;
    int m = INT_MIN;
    for (int i = n-1; i >= 0; i--){
      if (arr[i] >= m){
        m = arr[i];
        v.push_back(arr[i]);
      }
    }
    reverse(v.begin(), v.end());
    return v;
     
    
}
