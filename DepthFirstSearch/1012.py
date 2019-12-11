import sys
sys.setrecursionlimit(50000)

def dfs(i, j):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and cabbage[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny)


T = int(input())
for tc in range(T):
    answer = 0
    M, N, K = map(int, input().split())
    cabbage = [[0] * N for _ in range(M)]
    visited = [[False] * N for _ in range(M)]
    for xy in range(K):
        x, y = map(int, input().split())
        cabbage[x][y] = 1
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and cabbage[i][j]:
                answer += 1
                visited[i][j] = True
                dfs(i, j)
    print(answer)

# C++ Code
# #include<iostream>
# #include<cstring>
#
# using namespace std;
# int cabbage[51][51] = { 0, };
# bool visited[51][51] = { false, };
# int T, M, N, K, x, y, answer;
#
# void dfs(int x,int y) {
# 	int nx, ny;
# 	int dx[4] = { -1,0,1,0 };
# 	int dy[4] = { 0,1,0,-1 };
# 	for (int i = 0; i < 4; ++i) {
# 		nx = x + dx[i];
# 		ny = y + dy[i];
# 		if (!visited[nx][ny] && cabbage[nx][ny] && 0 <= nx && 0 <= ny && nx < M && ny < N) {
# 			visited[nx][ny] = true;
# 			dfs(nx, ny);
# 		}
# 	}
# }
#
# int main() {
# 	cin >> T;
# 	while(T--) {
# 		answer = 0;
# 		cin >> M >> N >> K;
# 		memset(cabbage, 0, sizeof(cabbage));
# 		memset(visited, false, sizeof(visited));
# 		for (int i = 0; i < K; ++i) {
# 			cin >> x >> y;
# 			cabbage[x][y] = 1;
# 		}
#
# 		for (int i = 0; i < M; ++i) {
# 			for (int j = 0; j < N; ++j) {
# 				if (!visited[i][j] && cabbage[i][j]) {
# 					answer++;
# 					visited[i][j] = true;
# 					dfs(i, j);
# 				}
# 			}
# 		}
# 		cout << answer << '\n';
# 	}
# }