
#include <iostream>
#include <algorithm>
using namespace std;

int C, N, average, sum, counter, students[1001];

int main()
{
    cout.precision(3);
    cout.setf(ios::showpoint);
    cout.setf(ios::fixed);
    cin >> C;
    while (C--)
    {
        cin >> N;
        sum = 0;
        counter = 0;
        for (int i = 0; i < N; ++i)
        {
            cin >> students[i];
            sum += students[i];
        }
        average = sum / N;
        for (int i = 0; i < N; ++i)
        {
            if (students[i] > average)
            {
                counter++;
            }
        }
        cout << (double)counter/N * 100 << "%\n";
    }
}


// C++ output forammting 
// cout.setf(ios::fixed) 고정 소수점 표시
// cout.precision 소수점 자리수 설정
// cout.setf(ios::showpoint) 소수점 자리수 표현

