#include<iostream>
#include<vector>
#include<ctime>
using namespace std;

void insertionSort(vector<int>& v) {
	for (int i = 1; i < v.size(); ++i) {
		int tmp = v[i];
		int j = i - 1;
		while (j >= 0 && tmp < v[j]) {
			v[j + 1] = v[j];
			j--;
		}
		v[j + 1] = tmp;
	}
}

void show(vector<int> v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

int main() {
	vector<int> b;
	for (int i = 0; i < 1000; i++) {
		b.push_back(rand() % 1000);
	}
	insertionSort(b);
	show(b);
}