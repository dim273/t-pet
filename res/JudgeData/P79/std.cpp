#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool carPooling(vector<vector<int>>& trips, int capacity) {
        int to_max = 0;
        for (const auto& trip : trips) {
            to_max = max(to_max, trip[2]);
        }
        vector<int> diff(to_max + 1, 0);
        for (const auto& trip : trips) {
            diff[trip[1]] += trip[0];
            diff[trip[2]] -= trip[0];
        }
        int count = 0;
        for (int i = 0; i <= to_max; ++i) {
            count += diff[i];
            if (count > capacity) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    int n;
    cin >> n;
    vector<vector<int>> trips(n, vector<int>(3));
    for (int i = 0; i < n; ++i) {
        cin >> trips[i][0] >> trips[i][1] >> trips[i][2];
    }
    int capacity;
    cin >> capacity;
    Solution sol;
    bool result = sol.carPooling(trips, capacity);
    cout << (result ? "true" : "false") << endl;
    return 0;
}