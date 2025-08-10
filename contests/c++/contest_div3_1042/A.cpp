#include <iostream>

using namespace std;


int trobarAmesgranqueB(int numbers1[], int numbers2[], int len){
    for(int i=0; i < len; i++){
        if(numbers1[i] > numbers2[i]){
            return i;
        }
    }
    return -1;
}

int trobarBmesgranqueA(int numbers1[], int numbers2[], int len){
    for(int i=0; i < len; i++){
        if(numbers1[i] < numbers2[i]){
            return i;
        }
    }
    return -1;
}


int main(){
    int t; // Number of cases 
    cin >> t;
    for(int i = 0; i<t; i++){
        int n; // longitud de les arrays que entren
        cin >> n;

        int array1[n];
        int array2[n];

        for(int i = 0; i < n; i++){
            cin >> array1[i];
        }

        for(int i = 0; i < n; i++){
            cin >> array2[i];
        }

        int jumps = 1;

       while (true) {
            int idxA = trobarAmesgranqueB(array1, array2, n);
            if (idxA == -1) {
                break; 
            }
            array1[idxA] -= 1;

            int idxB = trobarBmesgranqueA(array1, array2, n);
            if (idxB != -1) {
                array1[idxB] += 1;
            }
            jumps++;
        }
        cout << jumps << endl;
    }
}


