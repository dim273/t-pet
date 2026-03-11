#include <stdio.h>
#include <math.h>

int n;
double a[20], b[20];
double dp[65000][20];
bool v[20];
double ans = 1e9;

double dis(int x, int y) {
    return sqrt((a[x] - a[y]) * (a[x] - a[y]) + (b[x] - b[y]) * (b[x] - b[y]));
}

void dfs(int t, int now, double s, int state) {
    if (s > ans) return;
    if (t == n) {
        if (s < ans) ans = s;
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (!v[i]) {
            int p = state + (1 << (i - 1));
            double d = s + dis(now, i);
            if (dp[p][i] <= d) continue;
            dp[p][i] = d;
            v[i] = true;
            dfs(t + 1, i, d, p);
            v[i] = false;
        }
    }
}

int main() {
    scanf("%d", &n);
    a[0] = 0; b[0] = 0;
    for (int i = 1; i <= n; i++) {
        scanf("%lf%lf", &a[i], &b[i]);
    }
    for (int i = 0; i < 65000; i++) {
        for (int j = 0; j < 20; j++) {
            dp[i][j] = 1e9;
        }
    }
    dfs(0, 0, 0.0, 0);
    printf("%.2lf\n", ans);
    return 0;
}