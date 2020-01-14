#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, number;
vector<int> v[501];
int main()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < i + 1; ++j)
        {
            cin >> number;
            v[i].push_back(number);
        }
    }

    for (int i = n - 2; i >= 0; --i)
    {
        for (int j = 0; j < v[i].size(); ++j)
        {
            v[i][j] = max(v[i + 1][j], v[i + 1][j + 1]) + v[i][j];
        }
    }
    cout << v[0][0];
}