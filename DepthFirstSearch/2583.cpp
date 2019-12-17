#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int M, N, K, component = 0;
int map[101][101];
int visited[101][101];

int dfs(int i, int j, int c)
{
    int d[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    int nx, ny;
    for (int k = 0; k < 4; ++k)
    {
        nx = i + d[k][0];
        ny = j + d[k][1];
        if (0 <= nx && nx < M && 0 <= ny && ny < N && !map[nx][ny] && !visited[nx][ny])
        {
            visited[nx][ny] = true;
            c += dfs(nx, ny, 0) + 1;
        }
    }
    return c;
}

int main()
{
    cin >> M >> N >> K;
    int left, right, top, bottom;
    vector<int> area;
    for (int k = 0; k < K; ++k)
    {
        cin >> left >> top >> right >> bottom;
        for (int i = top; i < bottom; ++i)
        {
            for (int j = left; j < right; ++j)
            {
                map[i][j] = 1;
            }
        }
    }
    for (int i = 0; i < M; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            if (!map[i][j] && !visited[i][j])
            {
                visited[i][j] = true;
                component++;
                area.push_back(dfs(i, j, 1));
            }
        }
    }
    sort(area.begin(), area.end());
    cout << component<< '\n';
    for(int i=0;i<area.size();++i){
        cout << area[i] << " ";
    }
}