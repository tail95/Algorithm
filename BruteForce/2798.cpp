#include<iostream>
using namespace std;

int main() {
	int numCards, targetNumber;
	int* cards;
	cin >> numCards >> targetNumber;
	cards = new int[numCards];
	for (int i = 0; i < numCards; ++i) {
		cin >> cards[i];
	}
	int maxsum = 0;
	for (int i = 0; i < numCards-2; ++i) {
		for (int j = i+1; j < numCards-1; ++j) {
			for (int k = j+1; k < numCards; ++k) {
				int tmpNum = cards[i] + cards[j] + cards[k];
				if (tmpNum <= targetNumber && maxsum < tmpNum)
					maxsum = tmpNum;
            }
        }
	}
	cout << maxsum;
}