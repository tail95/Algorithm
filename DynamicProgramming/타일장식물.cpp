#include<iostream>
#include <string>
#include <vector>

using namespace std;

long long solution(int N) {
    long long answer = 0;
    long long d[80];
    d[0]=0;
    d[1]=2;
    d[2]=3;
    for(int i=3; i<= N; i++){
        d[i] = d[i-1] + d[i-2];
    }   
    answer = 2*d[N];
    return answer;
}