#include <iostream>
using namespace std;

int main(){
    int n;

    cin >> n;

    for (int i = 1; i <= n; i++) {
        for(int j = i+1; j <= n; j++){
            cout << ' ';
        }
        
        for(int k = n-i; k < n; k++){
            cout << '*';
        }

        cout << endl;
    }

    return 0;
}