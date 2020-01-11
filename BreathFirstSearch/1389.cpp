#include <iostream>
#include <algorithm>
#include <queue>
#include<vector>
using namespace std;

int N, M, x, y, tmp, depth, answer = 987654321, graph[101][101];
bool visited[101];
queue<pair<int, int>> q;
vector<int> v;

int main()
{
    cin >> N >> M;
    for (int i = 0; i < M; ++i)
    {
        cin >> x >> y;
        x--;
        y--;
        graph[x][y] = graph[y][x] = 1;
    }

    for (int i = 0; i < N; ++i)
    {
        tmp = 0;
        fill(&visited[0], &visited[101], false);
        q.push(make_pair(i, 1));
        visited[i] = true;
        while (!q.empty())
        {
            pair<int, int> front = q.front();
            
            q.pop();
            for (int j = 0; j < N; ++j)
            {
                if (graph[front.first][j] == 1 && !visited[j])
                {  
                    // cout << "Visit: " << j << endl;
                    // cout <<  " Depth: " << front.second << endl;
                    tmp+=front.second;
                    visited[j] = true;
                    q.push(make_pair(j, front.second+1));
                }
            }
        }
        // cout << tmp << " " << endl << endl;
        v.push_back(tmp);
        answer = min(answer, tmp);
    }
    
    for(int i=0;i<v.size();++i){
        if(v[i] == answer){
            cout << i + 1;
            break;
        }
    }
}