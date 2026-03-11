#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int findGoodStrings(int n, string s1, string s2, string evil) {
        const int MOD = 1e9 + 7;
        int m = evil.size();
        vector<int> next(m);
        for (int i = 1, j = 0; i < m; ++i) {
            while (j > 0 && evil[i] != evil[j]) j = next[j - 1];
            if (evil[i] == evil[j]) ++j;
            next[i] = j;
        }
        vector<vector<int>> memo(n, vector<int>(m + 1, -1));
        function<int(int, int, bool, bool)> dfs = [&](int i, int j, bool limitLow, bool limitHigh) -> int {
            if (i == n) return 1;
            if (!limitLow && !limitHigh && memo[i][j] != -1) return memo[i][j];
            char lo = limitLow ? s1[i] : 'a';
            char hi = limitHigh ? s2[i] : 'z';
            int res = 0;
            for (char d = lo; d <= hi; ++d) {
                int nj = j;
                while (nj > 0 && d != evil[nj]) {
                    nj = next[nj - 1];
                }
                if (d == evil[nj]) ++nj;
                if (nj == m) continue;
                res = (res + dfs(i + 1, nj, limitLow && d == lo, limitHigh && d == hi)) % MOD;
            }
            if (!limitLow && !limitHigh) memo[i][j] = res;
            return res;
        };
        return dfs(0, 0, true, true);
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    string s1, s2, evil;
    cin >> n >> s1 >> s2 >> evil;
    Solution sol;
    cout << sol.findGoodStrings(n, s1, s2, evil) << endl;
    return 0;
}