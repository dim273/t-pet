#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        if (arr[start] == 0) {
            return true;
        }
        
        int n = arr.size();
        vector<bool> used(n, false);
        queue<int> q;
        q.push(start);
        used[start] = true;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            if (u + arr[u] < n && !used[u + arr[u]]) {
                if (arr[u + arr[u]] == 0) {
                    return true;
                }
                q.push(u + arr[u]);
                used[u + arr[u]] = true;
            }
            if (u - arr[u] >= 0 && !used[u - arr[u]]) {
                if (arr[u - arr[u]] == 0) {
                    return true;
                }
                q.push(u - arr[u]);
                used[u - arr[u]] = true;
            }
        }
        return false;
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int start;
    cin >> start;
    Solution sol;
    bool result = sol.canReach(arr, start);
    cout << (result ? "true" : "false") << endl;
    return 0;
}