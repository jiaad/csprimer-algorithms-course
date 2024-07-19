#include <iostream>
using namespace std;

int main(void) {
  long long n;
  cin >> n;
  long long arr[n + 1];
  bool problem = false;

  long long i = 0;
  long long count = 2;

  while (count <= n) {
    arr[i++] = count;
    count += 2;
  }

  count = 1;
  while (count <= n) {
    arr[i++] = count += 2;
    count += 2;
  }

  i = 1;

  while (i < n) {
    if (abs(arr[i - 1] - arr[i]) == 1) {
      cout << "NO SOLUTION" << "\n";
      return 0;
    }
    i += 1;
  }

  i = 0;
  while (i < n) {
    cout << arr[i++] << " ";
  }
  cout << "\n";
  return 0;
}
