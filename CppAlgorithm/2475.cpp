#include <iostream>
using namespace std;

int main(){
    int result = 0;

    for (int i = 0; i < 5; i++){
        int temp_int;
        cin >> temp_int;

        result += temp_int * temp_int;
    }

    cout << result % 10;

    return 0;
}