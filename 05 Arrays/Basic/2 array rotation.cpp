#include<bits/stdc++.h>
using namespace std;

long long a[10000000];

void rotateArr(long long d, long long n){
    
    reverse(a, a+d);
    reverse(a+d, a+n);
    reverse(a, a+n);
    
}


int main() {
	//code
	
	long long t;
	cin >> t;
	
	while(t--){
	    long long n, d;
	    cin >> n >> d;
	    
	    for(long long i = 0; i < n; i++){
	        cin >> a[i];
	    }
	    
	    rotateArr(d,n);
	    
	    for(long long i =0;i<n;i++){
	        cout << a[i] << " ";
	    }
	    cout << endl;
	    
	}
	
	return 0;
}

