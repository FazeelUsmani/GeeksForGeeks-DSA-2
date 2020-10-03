#include <bits/stdc++.h>
using namespace std;

void permute(string str, int pos)
{

    if (pos == -1)
    {
        cout << str << endl;
        return;
    }

    else
    {
        for (int i = pos; i >= 0; --i)
        {
            swap(str[i], str[pos]);
            permute(str, pos - 1);
            swap(str[i], str[pos]);
        }
    }
}

int main()
{

    string str = "ABC";
    permute(str, str.size() - 1);

    return 0;
}