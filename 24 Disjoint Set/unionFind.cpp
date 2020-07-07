
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
// par : empty array (n+1) size with all elements as i
// rank1 : empty array (n+1) size with all elements as 1
void union_( int a, int b, int parent[], int rank1[]) {
    
    int x = find(parent, a);
    int y = find(parent, b);
    
    if (x != y){
        if (rank1[x] < rank1[x])
            swap(x, y);
        parent[y] = x;
        rank1[x] += rank1[y];
    }
}

/* This function checks whether 2 nodes x and y are connected or not */
// x : node 1 
// y : node 2
// par : empty array (n+1) size with all elements as i
// rank1 : empty array (n+1) size with all elements as 1
bool isConnected(int x,int y, int par[], int rank1[]) {
    
    return (find(par, x) == find(par, y));
}
