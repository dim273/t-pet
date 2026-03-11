#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordDictSet;
        for (const auto& word : wordDict) {
            wordDictSet.insert(word);
        }
        vector<bool> dp(s.size() + 1, false);
        dp[0] = true;
        for (int i = 1; i <= s.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordDictSet.find(s.substr(j, i - j)) != wordDictSet.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};

int main() {
    string s;
    cin >> s;
    int n;
    cin >> n;
    vector<string> wordDict(n);
    for (int i = 0; i < n; ++i) {
        cin >> wordDict[i];
    }
    Solution solution;
    cout << (solution.wordBreak(s, wordDict) ? "true" : "false") << endl;
    return 0;
}