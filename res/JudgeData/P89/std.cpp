#include <bits/stdc++.h>
using namespace std;
typedef long long LL;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T;
    cin >> T;
    const LL NEG_INF = -(1LL << 60);
    while (T--) {
        int n, m;
        cin >> n >> m;
        vector<vector<LL>> grid(n, vector<LL>(m));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> grid[i][j];
            }
        }
        int total_states = 1 << m;
        vector<vector<LL>> dp(n + 1, vector<LL>(total_states, NEG_INF));
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int s = 0; s < total_states; s++) {
                if (s & (s << 1)) continue; // 同一行内不能有相邻的1
                LL sum = 0;
                for (int j = 0; j < m; j++) {
                    if (s & (1 << j)) {
                        sum += grid[i - 1][j];
                    }
                }
                for (int prev = 0; prev < total_states; prev++) {
                    if (dp[i - 1][prev] == NEG_INF) continue;
                    // 检查与上一行的冲突（8邻域）
                    if (s & prev) continue;
                    if (s & (prev << 1)) continue;
                    if (s & (prev >> 1)) continue;
                    dp[i][s] = max(dp[i][s], dp[i - 1][prev] + sum);
                }
            }
        }
        LL ans = 0;
        for (int s = 0; s < total_states; s++) {
            ans = max(ans, dp[n][s]);
        }
        cout << ans << '\n';
    }
    return 0;
}