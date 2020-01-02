#include<iostream>
using namespace std;

int N, S, answer=0, numbers[21];
void dfs(int sum, int idx){
    sum += numbers[idx];
    if(idx >= N) return;
    if(sum == S) answer++;
    dfs(sum, idx+1);
    dfs(sum-numbers[idx],idx+1);
}

int main(){
    cin >> N >> S;
    for(int i=0;i<N;++i){
        cin >> numbers[i];
    }
    dfs(0,0);
    cout << answer;
}
// dfs를 통해 각 숫자의 합을 더해서 확인 


//// Python combination을 활용
// from itertools import combinations
// N, S = map(int, (input().split()))
// numbers = list(map(int, input().split()))
// cn = []
// for i in range(1, N+1):
//     cn.extend(list(combinations(numbers, i)))
// cnt = 0 
// for tmp in cn:
//     if sum(tmp) == S:
//         cnt += 1
// print(cnt)