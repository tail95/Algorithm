// # import sys
// # T = int(sys.stdin.readline())
 
// # while T:
// #     N = int(sys.stdin.readline())
// #     scores = []
// #     answer = []
// #     while N:
// #         scores.append(list(map(int, sys.stdin.readline().rstrip().split())))
// #         N-=1
// #     scores.sort()
// #     # print(scores)
// #     answer = 0
// #     tMax = 987654321
// #     for s in scores:
// #         if s[1] < tMax:
// #             tMax = s[1]
// #             answer += 1
// #     # print(test)
// #     print(answer)
     
// #     T -= 1

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;
int T, N, a, b, tMax, answer;
int v[100001][2];
int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
    cin >> T;
    while(T--){
        tMax = 987654321;
        answer = 0;
        cin >> N;
        for(int i=0;i<N;++i){
            cin >> a >> b;
            v[i][0] = a;
            v[i][1] = b;
        }
        sort(&v[0][0], &v[N][0]);
        for(int i=0;i<N;++i){
            if(v[i][1] < tMax){
                tMax = v[i][1];
                answer++;
            }
        }
        cout << answer << "\n";
    }

}


import sys
inp=sys.stdin.readline

while(True):
    try:
        tc = int(inp())
        break
    except:
        pass

for i in range(tc):
    while(True):
        try:
            n = int(inp())
            break
        except:
            pass
    a = []
    n_input = 0
    while(n_input<n):
        temp = list(map(int,inp().split()))
        if(len(temp) == 2):
            a.append(temp)
            n_input+=1
    a.sort()
    ans = 1
    deg = a[0][1]
    for j in range(1,len(a)):
        if(deg > a[j][1]):
            ans+=1
            deg = a[j][1]
    print (ans)
