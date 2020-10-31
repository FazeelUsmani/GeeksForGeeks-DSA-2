#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends


int kthSmallest(int arr[], int n, int k){
    priority_queue<int, vector<int>, greater<int>> pq (arr, arr+n);
    
    while (--k)
        pq.pop();
        
    return pq.top();
}

// { Driver Code Starts.
int main(){
	
	int t;
	cin >> t;
	while(t--){
	    
	    int n, k;
	    cin >> n >> k;
	    int arr[n];
	    
	    for(int i = 0; i<n; ++i)
	        cin>>arr[i];
	        
	    cout << kthSmallest(arr, n, k) << endl;
	    
	}
	return 0;
}  // } Driver Code Ends
