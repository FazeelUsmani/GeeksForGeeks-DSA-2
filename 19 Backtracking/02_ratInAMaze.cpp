#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> sol(3, (3, 0));

void printMatrix(vector < vector<int> & mat)
{
    for (int i = 0; i < mat.size(); ++i)
    {
        for (int j = 0; j < mat.size(); ++j)
        {
            cout << mat[i][j] << " ";
        }
        cout << endl;
    }
}

bool recurse(j f)

    bool ratMaze(vector < vector<int> & maze)
{
    if (recurse(0, 0) == false)
        return false;
    else
    {
        printMatrix(sol);
        return true;
    }
}

int main()
{

    vector<vector<int>> maze{{1, 0, 0, 0}, {1, 1, 0, 1}, {0, 1, 0, 0}, {1, 1, 1, 1}};

    cout << ratMaze(maze);

    return 0;
}