#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int K, V, N;
    cin >> K >> V >> N;
    vector<int> vol(N+1), val(N+1);
    for (int i = 1; i <= N; i++) {
        cin >> vol[i] >> val[i];
    }

    const int NEG_INF = -20021003;
    vector<vector<int>> dp(V+1, vector<int>(K+1, NEG_INF));
    for (int j = 0; j <= V; j++) dp[j][1] = 0; // base: volume 0, at least 1 solution

    for (int i = 1; i <= N; i++) {
        for (int j = V; j >= vol[i]; j--) {
            vector<int> now(K+1);
            int c1 = 1, c2 = 1, cnt = 0;
            while (cnt < K) {
                if (dp[j][c1] > dp[j - vol[i]][c2] + val[i])
                    now[++cnt] = dp[j][c1++];
                else
                    now[++cnt] = dp[j - vol[i]][c2++] + val[i];
            }
            for (int c = 1; c <= K; c++)
                dp[j][c] = now[c];
        }
    }

    int ans = 0;
    for (int i = 1; i <= K; i++) ans += dp[V][i];
    cout << ans << "\n";
    return 0;
}