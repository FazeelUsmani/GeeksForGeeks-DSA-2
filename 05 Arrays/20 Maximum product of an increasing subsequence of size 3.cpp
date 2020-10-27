#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll maxProduct(vector<int> A)
{
    int n = A.size();
    vector<int> smaller(n);
    smaller[0] = -1;
    set<int> S;
    for (int i = 0; i < n; i++)
    {
        auto j = S.insert(A[i]);
        auto curr = j.first;
        --curr;
        if (curr != S.end())
            smaller[i] = *curr;
        else
            smaller[i] = -1;
    }

    ll ans = LONG_MIN;
    ll max_right = A[n - 1];

    for (int i = n - 2; i >= 1; i--)
    {
        if (A[i] > max_right)
            max_right = A[i];

        else if (smaller[i] != -1)
            ans = max(ans, max_right * smaller[i] * A[i]);
    }

    return ans;
}
