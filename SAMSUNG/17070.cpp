
// 처음 푼 방식
// #include <iostream>
// using namespace std;
// int n, ncase = 0, maps[17][17];

// bool goRight(int headX, int headY){
//     return (maps[headY][headX+1] != 1) ? true : false;
// }

// bool goDiagonal(int headX, int headY){
//     return ((maps[headY+1][headX] != 1) && (maps[headY][headX+1] != 1) 
//             && (maps[headY+1][headX+1] != 1)) ? true :false;
// }

// bool goDown(int headX, int headY){
//     return ((maps[headY+1][headX] != 1)) ? true: false;
// }
// void forward(int stat, int headX, int headY)
// {
//     // cout << "stat: " << stat << " X: " << headX << " Y: "  << headY << endl;
//     if(((headX==n-1 && headY==n-2) && goDown(headX, headY) && (stat == 1 || stat == 2)) ||
//         ((headX==n-2 && headY==n-1) && goRight(headX, headY) && (stat == 0 || stat == 2)) ||
//         ((headX==n-2 && headY==n-2) && goDiagonal(headX, headY))){
//             // cout << "UP"<< endl;
//             ncase++;
//         }
//     else
//     {
//         switch (stat)
//         {
//         case 0: // 가로
//             if (goRight(headX, headY) && (headX + 1 < n - 1))
//             {
//                 forward(0, headX+1, headY);
//             }
//             if (goDiagonal(headX, headY) && (headX < n - 1) && (headY < n - 1))
//             {
//                 forward(2, headX+1, headY+1);
//             }
//             break;

//         case 1: // 세로
//             if (goDown(headX, headY) && (headY + 1 < n - 1))
//             {
//                 forward(1, headX, headY+1);
//             }
//             if (goDiagonal(headX, headY) && (headX < n - 1) && (headY < n - 1)){
//                 forward(2, headX+1, headY+1);
//             }
//             break;
//         case 2: // 대각선
//             if (goRight(headX, headY) && (headX + 1 < n - 1))
//             {
//                 forward(0, headX+1, headY);
//             }
//             if (goDown(headX, headY) && (headY + 1 < n - 1))
//             { 
//                 forward(1, headX, headY+1);
//             }
//             if (goDiagonal(headX, headY) && (headX < n - 1) && (headY < n - 1))
//             {
//                 forward(2, headX+1, headY+1);
//             }
//             break;
//         default:
//             break;
//         }
//     }
// }

// int main()
// {
//     int status = 0, headX = 1, headY = 0;
//     cin >> n;
//     for (int i = 0; i < n; ++i)
//     {
//         for (int j = 0; j < n; ++j)
//         {
//             cin >> maps[i][j];
//         }
//     }

    
//     // for (int i = 0; i < n; ++i)
//     // {
//     //     for (int j = 0; j < n; ++j)
//     //     {
//     //         cout << maps[i][j] << " ";
//     //     }
//     //     cout << endl;
//     // }
//     forward(status, headX, headY);
//     cout << ncase;
// }



#include <iostream>
using namespace std;
int n, ncase = 0, maps[17][17];

bool goRight(int headX, int headY){
    return (maps[headY][headX+1] != 1) ? true : false;
}

bool goDiagonal(int headX, int headY){
    return ((maps[headY+1][headX] != 1) && (maps[headY][headX+1] != 1) 
            && (maps[headY+1][headX+1] != 1)) ? true :false;
}

bool goDown(int headX, int headY){
    return ((maps[headY+1][headX] != 1)) ? true: false;
}
void forward(int stat, int headX, int headY)
{
    // cout << "stat: " << stat << " X: " << headX << " Y: "  << headY << endl;
    if(headX==n-1 && headY==n-1){
            // cout << "UP"<< endl;
            ncase++;

        }
    else
    {
        switch (stat)
        {
        case 0: // 가로
            if (goRight(headX, headY))
            {
                forward(0, headX+1, headY);
            }
            if (goDiagonal(headX, headY))
            {
                forward(2, headX+1, headY+1);
            }
            break;

        case 1: // 세로
            if (goDown(headX, headY))
            {
                forward(1, headX, headY+1);
            }
            if (goDiagonal(headX, headY)){
                forward(2, headX+1, headY+1);
            }
            break;
        case 2: // 대각선
            if (goRight(headX, headY))
            {
                forward(0, headX+1, headY);
            }
            if (goDown(headX, headY))
            { 
                forward(1, headX, headY+1);
            }
            if (goDiagonal(headX, headY))
            {
                forward(2, headX+1, headY+1);
            }
            break;
        default:
            break;
        }
    }
}

int main()
{
    int status = 0, headX = 1, headY = 0;
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> maps[i][j];
        }
    }
    // 잡기술 겉 테두리를 감싸서 체크할때 넘길 수 있음
    for (int i = 0; i < n; ++i)
    {
        maps[n][i] = 1;
        maps[i][n] = 1;
    }
    maps[n][n] =1;

    
    // for (int i = 0; i < n; ++i)
    // {
    //     for (int j = 0; j < n; ++j)
    //     {
    //         cout << maps[i][j] << " ";
    //     }
    //     cout << endl;
    // }
    forward(status, headX, headY);
    cout << ncase;
}