#include <iostream>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int current, nxt;
bool visited[201];

int solution(int n, vector<vector<int>> computers)
{
    int answer = 0;

    queue<int> q;
    for (int j = 0; j < computers.size(); ++j)
    {
        if (!visited[j])
        {
            answer++;
            q.push(j);
            visited[j] = true;
            while (!q.empty())
            {
                current = q.front();
                q.pop();
                for (int i = 0; i < computers[current].size(); ++i)
                {
                    if (!visited[i] && computers[current][i])
                    {
                        visited[i] = true;
                        q.push(i);
                    }
                }
            }
        }
    }
    return answer;
}

//// FOR TEST
// vector<vector<int>> v, v2;
// int main()
// {
//     v.resize(3);
//     v2.resize(3);
//     for (int i = 0; i < 3; ++i)
//     {
//         v[i].push_back(i);
//         v2[i].push_back(i);
//     }
//     v[0].push_back(1);
//     v[1].push_back(0);

//     v2[0].push_back(1);
//     v2[1].push_back(0);
//     v2[1].push_back(2);
//     v2[2].push_back(1);
    
//     // cout << solution(3, v) << endl;
//     cout << solution(3, v2) << endl;
// }
