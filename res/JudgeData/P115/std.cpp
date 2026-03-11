#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

struct Node {
    int w, v;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W, k;
    cin >> n >> W >> k;
    vector<Node> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i].w >> a[i].v;
    }

    sort(a.begin(), a.end(), [](const Node &x, const Node &y) {
        return x.w < y.w;
    });

    vector<int> f(W + 1, 0);
    int ans = 0;

    for (int i = 0; i < n; i++) {
        for (int j = W; j >= a[i].w; j--) {
            f[j] = max(f[j], f[j - a[i].w] + a[i].v);
        }
        priority_queue<int> q;
        for (int p = i + 1; p < n; p++) {
            q.push(a[p].v);
        }
        int now = f[W];
        int m = min((int)q.size(), k);
        while (m--) {
            now += q.top();
            q.pop();
        }
        ans = max(ans, now);
    }

    cout << ans << "\n";
    return 0;
}