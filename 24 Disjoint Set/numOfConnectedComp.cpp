
//User function Template for C++

int find(int parent[], int node){
    if (parent[node] == node)
        return node;
    parent[node] = find(parent, parent[node]);
    return parent[node];
}


/* This function does union of 2 nodes a and b */
// a : node 1 
// b : node 2
// arr : array (n+1) size with elements from 1 to N equal to its index.
// rank1 : array (n+1) size with all elements equal to 1. 
// n : Number of nodes
void unionNodes( int a, int b, int parent[], int size[], int n) {
    int c = find(parent, a);
    int d = find(parent, b);
    
    if (c != d){
        if (size[c] < size[d])
            swap(c, d);
        parent[d] = c;
        size[c] += size[d];
        --n;
    }
    
}

/* This function returns number of connected components */
// arr : array (n+1) size with elements from 1 to N equal to its index.
// rank1 : array (n+1) size with all elements equal to 1. 
// n : Number of nodes
int findNumberOfConnectedNodes( int n, int arr[], int rank1[]) {
    
    int cnt = 0;
    for (int i = 1; i <= n; ++i)
        if (arr[i] == i)
            ++cnt;
            
    return cnt;
}
