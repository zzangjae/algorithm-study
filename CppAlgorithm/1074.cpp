#include <iostream>
#include <cmath>

using namespace std;
int n, aim_r, aim_c, result;

void get_position(int r,int c,int depth){
    if (depth == 0){
        if (r == aim_r && c == aim_c) return;

        else if(r == aim_r && c+1 == aim_c) {
            result++;
            return;
        }

        else if(r+1 == aim_r && c == aim_c) {
            result+=2; 
            return;
        }

        else if(r+1 == aim_r && c+1 == aim_c){
            result+=3;
            return;
        }
    }

    if (r <= aim_r && aim_r < r + pow(2, depth)){
        if (c <= aim_c && aim_c < c + pow(2, depth)){
            get_position(r, c, depth-1);
        }
        else{
            result += pow(2, 2*depth);
            get_position(r, c + pow(2, depth), depth-1);
        }
    }
    else{
        if (c <= aim_c && aim_c < c + pow(2, depth)){
            result += pow(2, 2*depth) * 2;
            get_position(r + pow(2, depth), c, depth-1);
        }
        else{
            result += pow(2, 2*depth) * 3;
            get_position(r + pow(2, depth), c + pow(2, depth), depth-1);
        }
    }

}


int main(){
    cin >> n >> aim_r >> aim_c;
    get_position(0, 0, n-1);
    cout << result;
    return 0;
}