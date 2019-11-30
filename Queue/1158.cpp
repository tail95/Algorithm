#include<iostream>
#include<queue>
#include<vector>
#include<deque>
using namespace std;

deque<int> dq;
vector<int> v;
int main() {
	int N, K, index, count=0;
	cin >> N >> K;
	for (int i = 1; i <= N; ++i) {
		dq.push_back(i);
	}
	while (dq.size() > 0) {
		count++;
		if (count == K) {
			v.push_back(dq.front());
			dq.pop_front();
			count = 0;
			continue;
		}
		dq.push_back(dq.front());
		dq.pop_front();
	}

	cout << "<";
	for (int i = 0; i < v.size() -1; i++) {
		cout << v[i] << ", ";
	}
	cout << v[v.size() - 1];
	cout << ">";
}


// vector iterator를 활용한 방법
#include <iostream>
#include <vector>
using namespace std;
int main() {
	vector<int> v;
	int N, M;
	cin >> N >> M;
	for (int i = 1; i <= N; ++i)
		v.push_back(i);
	vector<int>::iterator it;
	it = v.begin();
	cout << "<";
	while (v.size() != 1) {
		for (int i = 0; i < M - 1; ++i) {
			++it;
			if (it == v.end())    // 끝까지돌면
				it = v.begin();  // 처음으로 
		}
		cout << *it << ", ";
		it = v.erase(it);
		if (it == v.end())
			it = v.begin();
	}
	cout << *it << ">";
}

