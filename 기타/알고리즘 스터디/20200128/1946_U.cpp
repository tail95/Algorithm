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