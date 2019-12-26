#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, targetA, targetB, m, x, y, current, nxt, d[101];
vector<vector<int>> v;
bool visited[101];
queue<int> q;
bool checker, fin;

void bfs(int ta, int tb)
{
    q.push(ta);
    visited[ta] = true;
    while (!q.empty())
    {
        current = q.front();
        q.pop();
        for (int i = 0; i < v[current].size(); ++i)
        {
            nxt = v[current][i];
            if (!visited[nxt])
            {
                q.push(nxt);
                visited[nxt] = true;
                d[nxt] = d[current] + 1;
            }
        }
    }
    cout << (d[tb] == 0 ? -1 : d[tb]) << endl;
}
int main()
{
    cin >> n >> targetA >> targetB >> m;
    v.resize(n);

    while (m--)
    {
        cin >> x >> y;
        v[x - 1].push_back(y - 1);
        v[y - 1].push_back(x - 1);
    }
    bfs(targetA - 1, targetB - 1);
}


// dp처럼 각 점으로 부터의 거리를 하나씩 추가해줘야함
