#include<iostream>
using namespace std;

int tiles[1001];

int main() {
	int n;
	cin >> n;
	tiles[1] = 1;
	tiles[2] = 2;
	for (int i = 3; i <= n; i++) {
		tiles[i] = (tiles[i - 1] + tiles[i - 2]) % 10007;   // overflow방지를 위해 나머지연산을 미리 해줘야함
	}
	cout << tiles[n] % 10007;
}