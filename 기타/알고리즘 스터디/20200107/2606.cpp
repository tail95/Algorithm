#include <iostream>

using namespace std;
int answer = 0, n, connect, x, y, graph[101][101];
bool visited[101];

void dfs(int x, int &answer)
{   
    for (int i = 0; i < n; ++i)
    {
        if (graph[x][i] && !visited[i])
        {
            visited[i] = true;
            answer++;
            dfs(i, answer);
        }
    }
}

int main()
{
    cin >> n >> connect;
    for (int i = 0; i < connect; ++i)
    {
        cin >> x >> y;
        graph[x - 1][y - 1] = graph[y - 1][x - 1] = 1;
    }
    visited[0] = true;
    dfs(0, answer);
    cout << answer;
}