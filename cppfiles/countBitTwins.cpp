#include <iostream>
#include <string>
using namespace std;

int countBitTwins(int num) {
  int count = 0;
  int mask = 0b110; // binary representation of twin pattern.
  while (num) {

    if ((num & mask) == mask) // check if the twin pattern is present
      count++;
    
    num >>= 1; // right shift the number until it becomes 0
  }
  return count;
}

int main() {
  string line;
  while (getline(cin, line)) {
    int num = stoi(line); // convert to integer
    int twins = countBitTwins(num);
    string twinsStr = to_string(twins);
    cout << twinsStr << endl;
  }
}
