#include <iostream>

using namespace std;

int main(){
    int t; // Number of cases 
    cin >> t;
    for(int i = 0; i<t; i++){
        int numberFruits;
        cin >> numberFruits;

        int x,y; // x is the blending power, y is the maximum amount of fruits the blender can enter.  
        cin >> x >> y;

        if(x == 0 || y == 0 || numberFruits == 0){
            cout << 0 << endl;
            continue;
        }

        int fruitsInBlender = 0;
        int calcul;



        if(x >= y){
            cout << ((numberFruits + y -1)  / y) << endl;
            continue;
        }

        if(x < y){
            cout << ((numberFruits + x -1) / x) << endl;
            continue;
        }
    }
}

