#include<list>
#include<iostream>
using namespace std;

int main() {
	int num;
	int* eureka;
	list<int> eurekanums;
	for (int i = 0; (i * (i + 1)) / 2 <= 1000; i++) eurekanums.push_back((i * (i + 1)) / 2);

	cin >> num;
	eureka = new int[num];
	for (int i = 0; i < num; i++) {
		cin >> eureka[i];
		int answer = 0;
		for (int x : eurekanums) {   // 향상된 for문 사용
			for (int y : eurekanums) {
				for (int z : eurekanums) {
					if (x + y + z == eureka[i]) {
						answer = 1;
					}
				}
			}
		}
		cout << answer << endl;
	}
	return 0;
}