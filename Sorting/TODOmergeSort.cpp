#include<iostream>
#include<vector>
#include<ctime>

using namespace std;

void show(vector<int> v) {
	for (int i = 0; i < v.size(); i++) {
		cout << v[i] << " ";
	}
	cout << endl;
}

void mergeSort(vector<int>& arr, int start, int center, int end) {
	vector<int> ret;
	int s = start, m = center + 1;
	int k = 0;
	cout << "\n\n\n";
	show(arr);
	while (start <= center && m <= end) {
		/*cout << "start:" << start << "\t m:" << m << "\t end:" << end << endl;
		cout << arr[start] << " " << arr[m] << endl;*/
		if (arr[start] < arr[m]) {
			ret.push_back(arr[start++]);
		}
		else if (arr[start] > arr[m]) {
			ret.push_back(arr[m++]);
		}
	}
	while (start <= center) {
		ret.push_back(arr[start++]);
		cout << arr[start] << endl;
	}
	while (m <= end) {
		ret.push_back(arr[m++]);
		cout << arr[m] << endl;
	}

	for (int t = s; t <= end; t++) {
		arr[t] = ret[k++];
	}
}
void merge(vector<int>& arr, int start, int end) {
	if (start < end) {
		int center = (start + end) / 2;
		merge(arr, start, center);
		merge(arr, center + 1, end);
		mergeSort(arr, start, center, end);
	}
}

int main() {
	srand(time(NULL));
	vector<int> a;
	for (int i = 0; i < 20; i++) {
		a.push_back(20 - i);
	}
	cout << "Before" << endl;
	show(a);
	cout << "----------------" << endl;
	merge(a, 0, 19);
	show(a);
}