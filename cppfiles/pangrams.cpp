#include <iostream>
#include <string>
#include <unordered_set>
using namespace std;

string missingLetters(string str) {
  unordered_set<char> letters;
  for (char c : str) { // build a set with all the letters in the string
    if (isalpha(c))
      letters.insert(tolower(c));
  }
  string missing;
  for (char c = 'a'; c <= 'z'; c++) { // check for missing letters in the set
    if (letters.count(c) == 0)
      missing += c;
  }
  if (missing.empty())
    return "NULL";
  return missing;
}

int main() {
  string line;
  while (getline(cin, line)) {
    string str = line;
    string pangramStr = missingLetters(str);
    cout << pangramStr << endl;
  }
}