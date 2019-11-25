#include<iostream>
#include<vector>
#include<ctime>
using namespace std;

template <typename T>
void bubbleSort(T& arr, int size) {
	for (int i = 0; i < size - 1; ++i) {
		for (int j = 0; j < size - 1 - i; ++j) {
			if (arr[j] > arr[j + 1]) {
				swap(arr[j], arr[j + 1]);
			}
		}
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
	bubbleSort(a, 5);
	show(a, 5);

	vector<int> b;
	for (int i = 0; i < 1000; i++) {
		b.push_back(rand() % 1000);
	}
	bubblesort(b, 1000);
	show(b, 1000);
}