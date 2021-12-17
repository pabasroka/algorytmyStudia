#include <iostream>

using namespace std;

void insertionSort(int arr[8]) 
{
    for (int i = 1; i < 8; i++) {
        int k = arr[i];
        int j = i - 1;
        while(j >= 0 && k < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = k;
    }
}

int main()
{
    int arr [8] = {1, -32, -21, 4, 0, 5, 7, 2};
    
    insertionSort(arr);
    
    for (int i = 0; i < 8; i++) {
        cout << arr[i] << " ";
    }
    
    return 0;
}