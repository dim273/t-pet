#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m;
    cin >> n >> m;
    vector<vector<int>> p(m + 1, vector<int>(n + 1));
    vector<vector<int>> rnk(n + 1, vector<int>(m + 1));
    for (int i = 1; i <= m; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> p[i][j];
            rnk[p[i][j]][i] = j;
        }
    }
    const int LOG = 19;
    vector<vector<vector<int>>> f(n + 1, vector<vector<int>>(LOG + 1, vector<int>(m + 1)));
    vector<vector<vector<vector<int>>>> h(m + 1, vector<vector<vector<int>>>(n + 2, vector<vector<int>>(LOG + 1, vector<int>(m + 1, INT_MAX))));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            f[i][0][j] = rnk[i][j];
        }
    }
    for (int i = 0; i <= LOG; i++) {
        for (int k = 1; k <= m; k++) {
            for (int u = 1; u <= m; u++) {
                for (int v = n; v >= 1; v--) {
                    h[u][v][i][k] = min(v == n ? INT_MAX : h[u][v + 1][i][k], f[p[u][v]][i][k]);
                }
            }
        }
        if (i == LOG) break;
        for (int x = 1; x <= n; x++) {
            for (int k = 1; k <= m; k++) {
                f[x][i + 1][k] = INT_MAX;
                for (int j = 1; j <= m; j++) {
                    f[x][i + 1][k] = min(f[x][i + 1][k], h[j][f[x][i][j]][i][k]);
                }
            }
        }
    }
    int Q;
    cin >> Q;
    while (Q--) {
        int x, y;
        cin >> x >> y;
        int ans = 0;
        bool beg = false, ok = false;
        vector<int> t(m + 1), nxt(m + 1);
        for (int i = LOG; i >= 0; i--) {
            if (!beg) {
                for (int j = 1; j <= m; j++) nxt[j] = f[x][i][j];
            } else {
                for (int j = 1; j <= m; j++) {
                    nxt[j] = INT_MAX;
                    for (int k = 1; k <= m; k++) {
                        nxt[j] = min(nxt[j], h[k][t[k]][i][j]);
                    }
                }
            }
            bool vld = false;
            for (int j = 1; j <= m; j++) {
                if (nxt[j] <= rnk[y][j]) {
                    vld = true;
                    break;
                }
            }
            if (vld) {
                ok = true;
            } else {
                ans += (1 << i);
                beg = true;
                t = nxt;
            }
        }
        if (!ok) cout << -1 << "\n";
        else cout << ans + 1 << "\n";
    }
    return 0;
}