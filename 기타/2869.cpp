#include<iostream>
#include<math.h>
using namespace std;
int a,b,v;
int main(){
    cin >> a >> b >> v;
    if(v-a<0) cout << 1;
    else{
        cout << (int)ceil((double)(v-a)/(a-b)) + 1;
    }
}

// (v-a)/(a-b)를 하면 int형 이기 때문에 double로 형변환 해야 하며
// ceil함수를 사용할 경우 실수형을 리턴하기때문에 int로 형변환해야한다.