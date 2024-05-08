#include <stdio.h>
void swap(int *a, int *b) {
  int tmp = *a;
  *a = *b;
  *b = tmp;
}
int main(void) {
  int arr[] = {10, 2, 34, 5, 562, 4, 34, 53, 6, 24, 23};
  int i;

  for (i = 0; i < sizeof(arr) / sizeof(int); i++) {
    int j = i;
    while ((j > 0) && (arr[j] < arr[j - 1])) {
      swap(&arr[j], &arr[j - 1]);
      j--;
    }
  }
  for (i = 0; i < (sizeof(arr) / sizeof(int)); i++) {
    printf("%d\n", arr[i]);
  }
}
