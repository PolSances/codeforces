#include <iostream>

using namespace std;


void printArray(int array[], int length){
    for(int i = 0; i < length; i++){
        cout << array[i] << " ";
    }
    cout << endl;
}

int main(){
    int t; // Number of cases 
    cin >> t;
    for(int i = 0; i<t; i++){
        int n;
        cin >> n;

        int array[n];

        if(n == 2){
            array[0] = -1;
            array[1] = 2;
            printArray(array, n);
            continue;
        }

        for(int i = 0; i < n; i++){
            if(i % 2 == 0){
                array[i] = -1;
            }
            else{
                array[i] = 3;
            }
        }
        printArray(array, n);
    }
}
