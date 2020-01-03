#include<iostream>
#include<vector>
#include<stack>
using namespace std;

int n, number, counter = 1;
vector<char> v;
stack<int> s;


int main(){
    cin >> n;
    for(int i=0;i<n;++i){
        cin >> number;
        if(s.empty() || s.top() < number){
            for(int j=counter; j<=number; ++j){
                s.push(j);
                v.push_back('+');
            }
            counter = number + 1;
        }
        if(s.top() == number){
            s.pop();
            v.push_back('-');
        }
        else{
            cout << "NO";
            return 0;
        }
    }

    for(int i=0;i<v.size();++i){
        cout << v[i] << '\n';
    }
}