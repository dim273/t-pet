#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
public:
    int prefixCount(vector<string>& words, string pref) {
        int res = 0;
        for (string & word : words) {
            if (word.compare(0, pref.size(), pref) == 0) {
                res++;
            }
        }
        return res;
    }
};

int main() {
    int n;
    cin >> n;
    vector<string> words(n);
    for (int i = 0; i < n; i++) {
        cin >> words[i];
    }
    string pref;
    cin >> pref;
    
    Solution sol;
    int ans = sol.prefixCount(words, pref);
    cout << ans << endl;
    
    return 0;
}