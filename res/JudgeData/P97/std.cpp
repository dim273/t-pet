#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool repeatedSubstringPattern(string s) {
        return (s + s).find(s, 1) != s.size();
    }
};

int main() {
    string s;
    while (cin >> s) {
        Solution sol;
        bool result = sol.repeatedSubstringPattern(s);
        cout << (result ? "true" : "false") << endl;
    }
    return 0;
}