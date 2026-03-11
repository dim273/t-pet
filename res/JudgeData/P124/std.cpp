#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, W, k;
    cin >> n >> W >> k;
    vector<pair<int,int>> gems(n);
    for (int i = 0; i < n; i++) {
        cin >> gems[i].first >> gems[i].second;
    }
    sort(gems.begin(), gems.end());

    vector<int> dp(W+1, 0);
    int ans = 0;

    for (int i = 0; i < n; i++) {
        for (int w = W; w >= gems[i].first; w--) {
            dp[w] = max(dp[w], dp[w - gems[i].first] + gems[i].second);
        }
        priority_queue<int> pq;
        for (int j = i+1; j < n; j++) {
            pq.push(gems[j].second);
        }
        int cur = dp[W];
        int take = min((int)pq.size(), k);
        for (int t = 0; t < take; t++) {
            cur += pq.top();
            pq.pop();
        }
        ans = max(ans, cur);
    }

    cout << ans << "\n";
    return 0;
}