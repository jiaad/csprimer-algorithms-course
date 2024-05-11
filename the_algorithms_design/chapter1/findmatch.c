#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int findmatch(char *p, char *t){
  int i;
  int j;
  int m;
  int n;
  m = strlen(p); // m
  n = strlen(t); // n
  for (i = 0; i <= (n - m); i++){ // n - m
    j = 0;
    while((j < m) && (t[i+j] == p[j])) // m
      j = j + 1;
    if(j == m) return (i);
  }

  // O(m + m + (n - m)(m + 2))
  // m + 2 -> 0(m)
  // now O(n + m + (n - m)m) -> O(n + m + nm - mˆ2)
  // 
  return -1;
}

int main(void){
  char t[] = "hello brother";
  char p[] = "brother";
  int res = findmatch(p, t);
  printf("res -> %d\n", res);
  return 0;
}
