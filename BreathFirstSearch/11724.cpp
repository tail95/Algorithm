#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int N, M, from, to;
vector<vector<int>> graph;
bool visited[1001];

void bfs(int idx)
{
    queue<int> q;
    q.push(idx);
    visited[idx] = true;
    while (!q.empty())
    {
        int current = q.front();
        q.pop();
        for (int i = 0; i < graph[current].size(); ++i)
        {
            int next = graph[current][i];
            if (!visited[next])
            {
                q.push(next);
                visited[next] = true;
            }
        }
    }
}

int main()
{
    cin >> N >> M;
    graph.resize(N + 1);
    for (int i = 0; i < M; ++i)
    {
        cin >> from >> to;
        graph[from - 1].push_back(to - 1);
        graph[to - 1].push_back(from - 1);
    }
    int answer = 0;
    for (int i = 0; i < N; ++i)
    {
        if (!visited[i])
        {
            bfs(i);
            answer++;
        }
    }
    cout << answer;
}