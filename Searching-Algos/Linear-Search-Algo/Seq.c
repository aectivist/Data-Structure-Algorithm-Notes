#include <stdio.h>

int search (int arr[], int N, int x){ //Sequential Search
    for (int i = 0; i < N; i++)
        if (arr[i] == x)
        return i;
    return -1;
}
 
int main(void){ // Setup and Output
    int arr[] = {2,10,3,14,32,29,12,16,53,23};
    int x = 10;
    int N = sizeof(arr) / sizeof(arr[0]);

//function output

int result = search(arr, N, x);
(result == -1)
    ? printf("Element != array") //note: ? is conditional operator equivalent to if TRUE
    : printf("Element = in array at index %d", result); //whereas : is equivalent to else if FALSE
    return 0;
}