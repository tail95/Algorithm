#include<iostream>
#include<algorithm>
using namespace std;
int n, scores[305], dp[305];
int main(){
    cin >> n;
    for(int i =3;i<=n;++i) cin >> scores[i];
    for(int i=3;i<=n;++i){
        dp[i] = max(dp[i-1], dp[i-2]) +dp[i-3] + scores[i]; 
    }
    for(int i=0;i<=n;++i){
        cout << dp[i] << " ";
    }
    // cout << dp[n];
}