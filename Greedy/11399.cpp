#include<iostream>
#include<algorithm>
using namespace std;

int N, answer = 0, tmp, withdraw[1001];
int main(){
    cin >> N;
    for(int i=0;i<N;++i){
        cin >> withdraw[i];
    }
    sort(&withdraw[0], &withdraw[N]);
    for(int i=0;i<N;++i){
        tmp = 0;
        for(int j=0;j<=i;++j){
            tmp+=withdraw[j];
        }
        answer+=tmp;
    }
    cout << answer;
}