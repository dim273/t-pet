#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        int n = rooms.size(), num = 0;
        vector<int> vis(n, 0);
        queue<int> que;
        vis[0] = 1;
        que.push(0);
        while (!que.empty()) {
            int x = que.front();
            que.pop();
            num++;
            for (auto& it : rooms[x]) {
                if (!vis[it]) {
                    vis[it] = 1;
                    que.push(it);
                }
            }
        }
        return num == n;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n;
    if (!(cin >> n)) return 0;
    vector<vector<int>> rooms(n);
    string line;
    getline(cin, line); // consume newline after n
    for (int i = 0; i < n; i++) {
        getline(cin, line);
        stringstream ss(line);
        int key;
        while (ss >> key) {
            rooms[i].push_back(key);
        }
    }
    
    Solution sol;
    bool result = sol.canVisitAllRooms(rooms);
    cout << (result ? "true" : "false") << endl;
    return 0;
}