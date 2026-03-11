#include <iostream>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return helper(nums, 0, nums.size() - 1);
    }
    TreeNode* helper(vector<int>& nums, int left, int right) {
        if (left > right) {
            return nullptr;
        }
        int mid = (left + right) / 2;
        TreeNode* root = new TreeNode(nums[mid]);
        root->left = helper(nums, left, mid - 1);
        root->right = helper(nums, mid + 1, right);
        return root;
    }
};

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    Solution sol;
    TreeNode* root = sol.sortedArrayToBST(nums);
    // 输出结果（层序遍历，null 用 -1 表示）
    if (!root) {
        cout << -1 << endl;
        return 0;
    }
    vector<TreeNode*> q;
    q.push_back(root);
    bool first = true;
    while (!q.empty()) {
        TreeNode* node = q.front();
        q.erase(q.begin());
        if (!first) cout << " ";
        first = false;
        if (node == nullptr) {
            cout << -1;
        } else {
            cout << node->val;
            q.push_back(node->left);
            q.push_back(node->right);
        }
    }
    cout << endl;
    return 0;
}