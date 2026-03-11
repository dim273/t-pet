#include <iostream>
#include <vector>
#include <string>
#include <cctype>

using namespace std;

class Solution {
public:
    vector<bool> camelMatch(vector<string>& queries, string pattern) {
        int n = queries.size();
        vector<bool> res(n, true);
        for (int i = 0; i < n; i++) {
            int p = 0;
            for (auto c : queries[i]) {
                if (p < pattern.size() && pattern[p] == c) {
                    p++;
                } else if (isupper(c)) {
                    res[i] = false;
                    break;
                }
            }
            if (p < pattern.size()) {
                res[i] = false;
            }
        }
        return res;
    }
};

int main() {
    int n;
    cin >> n;
    vector<string> queries(n);
    for (int i = 0; i < n; i++) {
        cin >> queries[i];
    }
    string pattern;
    cin >> pattern;
    
    Solution sol;
    vector<bool> ans = sol.camelMatch(queries, pattern);
    
    for (int i = 0; i < ans.size(); i++) {
        cout << (ans[i] ? "true" : "false");
        if (i != ans.size() - 1) {
            cout << " ";
        }
    }
    cout << endl;
    
    return 0;
}