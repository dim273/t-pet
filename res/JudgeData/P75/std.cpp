#include <iostream>
#include <vector>
using namespace std;

class NumArray {
public:
    vector<int> sums;

    NumArray(vector<int>& nums) {
        int n = nums.size();
        sums.resize(n + 1);
        for (int i = 0; i < n; i++) {
            sums[i + 1] = sums[i] + nums[i];
        }
    }

    int sumRange(int left, int right) {
        return sums[right + 1] - sums[left];
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    NumArray numArray(nums);
    
    int q;
    cin >> q;
    while (q--) {
        int left, right;
        cin >> left >> right;
        cout << numArray.sumRange(left, right) << endl;
    }
    
    return 0;
}