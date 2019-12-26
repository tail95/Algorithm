#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, targetA, targetB, m, x, y, current, nxt, answer = 0;
vector<vector<int>> v;
bool visited[101];
queue<int> q;
bool checker, fin;

void bfs(int ta, int tb)
{
    q.push(ta);
    visited[ta] = true;
    fin = false;
    while (!q.empty())
    {
        checker = false;
        current = q.front();

        cout << "Current Node: " << current << "\tanswer: " << answer << endl;
        q.pop();
        for (int i = 0; i < v[current].size(); ++i)
        {
            nxt = v[current][i];
            cout << i << endl;
            // cout << " NEXT: " << nxt << endl;
            if (!visited[nxt])
            {
                cout << " NEXT: " << nxt << endl;
                q.push(nxt);
                visited[nxt] = true;
                checker = true;
                if (nxt == tb)
                {
                    fin = true;
                    break;
                }
            }
        }
        if (checker)
            answer++;
        if(fin)
            break;
    }
    if (fin)
        cout << answer;
    else
        cout << -1;
}
int main()
{
    cin >> n >> targetA >> targetB >> m;
    v.resize(n + 1);
    while (m--)
    {
        cin >> x >> y;
        v[x - 1].push_back(y - 1);
        v[y - 1].push_back(x - 1);
    }
    bfs(targetA - 1, targetB - 1);
}