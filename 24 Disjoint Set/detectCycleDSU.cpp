
// User function Template for C++
int find(int parent[], int node){
    if (parent[node] == node)
        return node;
    parent[node] = find(parent, parent[node]);
    return parent[node];
}

bool unionNodes(int a, int b, int parent[], int size[]){
    int c = find(parent, a);
    int d = find(parent, b);
    if (c != d){
        if (size[c] < size[d])
            swap(c, d);
        parent[d] = c;
        size[c] += size[d];
        
        return false;
    }
    return true;
}

/*  Function to check if there is cycle in graph
*   adj[]: array of vectors to represent graph
*   n and e are number of nodes and edges respectively
*   parent[]: array to store parent of nodes. Each index stores its node value
* initially
*   rank1[]: Each node from 1 to n store initial size as 1.
*/
bool findCycle(vector<int> adj[], int parent[], int rank1[], int n, int e) {
    
    if (n < 3 || e < 3)
        return false;
    
    for (int i = 1; i <= n; ++i)
        for(auto it=adj[i].begin();it!=adj[i].end();it++)
            if(i<*it && unionNodes(i,*it,parent,rank1))
                return true;
    return false;
}
