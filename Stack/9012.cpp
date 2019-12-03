#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main() {
	int T;
	cin >> T;
	string tmp;
	for (int i = 0; i < T; ++i) {
		stack<char> s;
		bool vps=true;
		cin >> tmp;
		for (int j = 0; j < tmp.length(); ++j) {
			if (tmp[j] == '(') s.push(tmp[j]);
			else if (tmp[j] == ')' && !s.empty() && s.top() == '(') s.pop();
			else {
				vps = false;
				break;
			}
		}
		if (s.empty() && vps) cout << "YES" << endl;
		else cout << "NO"<< endl;
	}
}


