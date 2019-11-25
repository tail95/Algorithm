#include<iostream>
#include<vector>
#include<ctime>

using namespace std;

template <typename T>
void selectionSort(T& arr, int size) {
	for (int i = 0; i < size - 1; ++i) {
		//T min = arr[i]; 최솟값을 알 필요는 없다.
		int index = i;
		for (int j = i; j < size; ++j) {
			if (arr[j] < arr[i]) {
				//min = arr[j]; 최솟값을 알 필요는 없다.
				index = j;
			}
		}
		swap(arr[i], arr[index]);
	}
}

template <typename T>
void show(T arr, int size) {
	for (int i = 0; i < size; i++) {
		cout << arr[i] << " ";
	}
	cout << endl;
}

int main() {
	srand(time(NULL));
	char a[5] = { 'a', 'e', 'g', 'k', 'o' };
	selectionSort(a, 5);
	show(a, 5);

	vector<int> b;
	for (int i = 0; i < 1000; i++) {
		b.push_back(rand() % 1000);
	}
	selectionSort(b, 1000);
	show(b, 1000);
}