#include<list>
#include<iostream>
using namespace std;

int main() {
	int num;
	int* eureka;
	list<int> eurekanums;
	int index = 1;
	while (true) {
		int eurekanum = (index * (index + 1)) / 2;
		if (eurekanum > 1000) break;
		eurekanums.push_back(eurekanum);
		index++;
	}	

	cin >> num;
	eureka = new int[num];
	for (int i = 0; i < num; i++) {
		cin >> eureka[i];
		list<int>::iterator x;
		bool flag = false;
		for (x = eurekanums.begin(); x != eurekanums.end(); x++) {
			list<int>::iterator y;
			for (y = eurekanums.begin(); y != eurekanums.end(); y++) {
				list<int>::iterator z;
				for (z = eurekanums.begin(); z != eurekanums.end(); z++) {
					if (*x + *y + *z == eureka[i]) flag = true;
				}
			}
		}
		if (flag) cout << 1 << endl;
		else cout << 0 << endl;
	}

}