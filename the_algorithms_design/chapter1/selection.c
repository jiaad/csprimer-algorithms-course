#include <stdio.h>
#include <stdlib.h>

void selection_sort(int arr[], int len){
  int i;
  int j;
  int min;

  // The outer loop goes around N times
  // the nested loop goes around n - i - 1 times
  for(i = 0; i < len; i++){
    min = i;
    for(j = i + 1; j < len; j++){
      if(arr[j] < arr[min]){
        min = j;
      }
    }
    int temp = arr[min];
    arr[min] = arr[i];
    arr[i] = temp;
  }
}

int main(void) { 

  int arr[10] = {11,90,10,9,6,2,6,1,4,5};
  int i = 0;
  selection_sort(arr, 10);
  for(i = 0; i < 10; i++){
    printf("%d\n", arr[i]);
  }
  return 0; }
