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

vector<int> mergeSort(vector<int>& arr, int start, int center, int end) {
	vector<int> ret;
	cout << "\n\n\n";
	show(arr);
	while (true) {
		cout << "start:" << start << "\t center+1:" << center + 1 << "\t end:" << end<< endl;
		cout << arr[start] << " " << arr[center + 1] << endl;
		
		if (start == center && center + 1 == end) {
			cout << "OUT" << endl;
			break;
		}
		
		if (arr[start] < arr[center + 1]) {
			ret.push_back(arr[start]);
			cout << arr[start];
			start++;
		}
		else if (arr[start] > arr[center + 1]) {
			ret.push_back(arr[center + 1]);
			cout << arr[center + 1];
			center++;
		}
		
	}
	cout << "TEST";
	return ret;
}
void merge(vector<int>& arr, int start, int end) {
	vector<int> b;
	if (start < end) {
		int center = (start + end) / 2;
		merge(arr, start, center);
		merge(arr, center + 1, end);
		b = mergeSort(arr, start, center, end);
		show(b);
	}
}



int main() {
	srand(time(NULL));
	vector<int> a;
	for (int i = 0; i < 20; i++) {
		a.push_back(rand() % 20);
	}
	cout << "Before" << endl;
	show(a);
	cout << "----------------" << endl;
	merge(a, 0, 20);
	show(a);
	
}