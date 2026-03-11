#include <iostream>
#include <string>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        int n = s.size();
        if (n % 2 == 1) {
            return false;
        }

        unordered_map<char, char> pairs = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };
        stack<char> stk;
        for (char ch: s) {
            if (pairs.count(ch)) {
                if (stk.empty() || stk.top() != pairs[ch]) {
                    return false;
                }
                stk.pop();
            }
            else {
                stk.push(ch);
            }
        }
        return stk.empty();
    }
};

int main() {
    string line;
    getline(cin, line);
    
    string s_input;
    size_t pos = line.find('=');
    if (pos != string::npos) {
        s_input = line.substr(pos + 1);
    } else {
        s_input = line;
    }
    
    while (!s_input.empty() && (s_input.front() == ' ' || s_input.front() == '"')) {
        s_input.erase(0, 1);
    }
    while (!s_input.empty() && (s_input.back() == ' ' || s_input.back() == '"')) {
        s_input.pop_back();
    }
    
    Solution sol;
    bool result = sol.isValid(s_input);
    cout << (result ? "true" : "false") << endl;
    
    return 0;
}