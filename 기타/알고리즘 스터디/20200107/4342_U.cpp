#include <iostream>
#include <algorithm>
using namespace std;

int x, y, answer, counter;

int main()
{
    while (true)
    {
        cin >> x >> y;
        if (x == 0 && y == 0)
            break;
        counter = 0;
        while (true)
        {
            // cout << "x: " << x << " y: " << y << endl;
            if (x == 0 || y == 0)
                break;
            if (x < y)
                swap(x, y);
            if(x%y==0){
                x=x%y;
            }
            else{
                if(x/y>=2){
                    x =0;
                }
                else{
                    x=x-y;
                }
            }
            counter++;
        }
        cout << (counter % 2 == 0 ? "B" : "A") << " wins\n";
    }
}

// 이기기 위한 최적의 방법을 찾아야 하는 문제
// 풀이가 어려워 질문에서 힌트참고
// 1. a % b == 0일 때: 고민할 필요 없죠? a를 0 만들고 이기면 되겠죠.
// 2. a % b != 0일 때:
//     2.1 a / b >= 2일 때
//         여기서 중요한 건 이 상황에서 상대방에게 b, a%b라는 상황을 만들어 줄 것인지 만들게 할 것인지 선택할 수 있단 거여요. 즉, b, a%b가 이기든 지든 무조건 이겨요.
//     2.2 a / b < 2일 때
//         할 수 있는 게 하나 밖에 없으니까(그러니까 b, a - b) 그거 하고 나서 남은 상황이 지는지 이기는지 따져봐야겠죠.