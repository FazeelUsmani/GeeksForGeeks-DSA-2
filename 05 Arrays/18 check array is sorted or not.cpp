{
#include<bits/stdc++.h>
using namespace std;
//Position this line where user code will be pasted.
int main()
 {
	int T;
	cin>> T;
	
	while (T--){
	    int num;
        cin>>num;
        int arr[num];
        for(int i = 0; i<num; ++i)
            cin>>arr[i];
        
        bool flag = false;
        
        flag = checkRotatedAndSorted(arr, num);
        
        if(!flag){
            cout << "No"<<endl;
        }
        else
        cout << "Yes"<<endl;
    
	}
	
	return 0;
}
}
/*This is a function problem.You only need to complete the function given below*/
// arr: input array
// num: length of array
// This function returns true or false
bool checkRotatedAndSorted(int arr[], int n){
 
    int minEle = INT_MAX; 
    int maxEle = INT_MIN; 
  
    int minIndex = -1; 
  
    // Find the minimum element 
    // and it's index 
    for (int i = 0; i < n; i++) { 
        if (arr[i] < minEle) { 
            minEle = arr[i]; 
            minIndex = i; 
        } 
    } 
  
    int flag1 = 1; 
  
    // Check if all elements before minIndex 
    // are in increasing order 
    for (int i = 1; i < minIndex; i++) { 
        if (arr[i] < arr[i - 1]) { 
            flag1 = 0; 
            break; 
        } 
    } 
  
    int flag2 = 1; 
  
    // Check if all elements after minIndex 
    // are in increasing order 
    for (int i = minIndex + 1; i < n; i++) { 
        if (arr[i] < arr[i - 1]) { 
            flag2 = 0; 
            break; 
        } 
    } 
  
    // Check if last element of the array 
    // is smaller than the element just 
    // before the element at minIndex 
    if (flag1 && flag2 && (arr[n - 1] < arr[minIndex - 1])) 
        return true;
    return false;
} 
