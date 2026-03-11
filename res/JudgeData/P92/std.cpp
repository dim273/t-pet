#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

class Solution {
public:
    vector<vector<int>> ans;
    vector<int> stk;

    void dfs(vector<vector<int>>& graph, int x, int n) {
        if (x == n) {
            ans.push_back(stk);
            return;
        }
        for (auto& y : graph[x]) {
            stk.push_back(y);
            dfs(graph, y, n);
            stk.pop_back();
        }
    }

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        stk.push_back(0);
        dfs(graph, 0, graph.size() - 1);
        return ans;
    }
};

int main() {
    int n;
    cin >> n;
    vector<vector<int>> graph(n);
    for (int i = 0; i < n; ++i) {
        int k;
        cin >> k;
        graph[i].resize(k);
        for (int j = 0; j < k; ++j) {
            cin >> graph[i][j];
        }
    }

    Solution sol;
    vector<vector<int>> paths = sol.allPathsSourceTarget(graph);

    for (const auto& path : paths) {
        for (size_t i = 0; i < path.size(); ++i) {
            if (i > 0) cout << " ";
            cout << path[i];
        }
        cout << "\n";
    }

    return 0;
}