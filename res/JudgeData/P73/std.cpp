#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int quickselect(vector<int>& nums, int l, int r, int k) {
        while (true) {
            if (l == r) return nums[k];
            int pivot = nums[l];
            int i = l - 1, j = r + 1;
            while (i < j) {
                do i++; while (nums[i] < pivot);
                do j--; while (nums[j] > pivot);
                if (i < j) swap(nums[i], nums[j]);
            }
            if (k <= j) {
                r = j;
            } else {
                l = j + 1;
            }
        }
    }

    int findKthLargest(vector<int>& nums, int k) {
        int n = nums.size();
        return quickselect(nums, 0, n - 1, n - k);
    }
};

int main() {
    int n, k;
    cin >> n >> k;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    Solution sol;
    int result = sol.findKthLargest(nums, k);
    cout << result << endl;
    return 0;
}