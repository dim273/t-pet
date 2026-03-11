#include <iostream>
#include <climits>

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
    bool helper(TreeNode* root, long long lower, long long upper) {
        if (root == nullptr) {
            return true;
        }
        if (root->val <= lower || root->val >= upper) {
            return false;
        }
        return helper(root->left, lower, root->val) && helper(root->right, root->val, upper);
    }
    bool isValidBST(TreeNode* root) {
        return helper(root, LLONG_MIN, LLONG_MAX);
    }
};

// Helper function to create a tree from level order input
TreeNode* createTree(int n, int idx, int* arr) {
    if (idx >= n || arr[idx] == -1) {
        return nullptr;
    }
    TreeNode* root = new TreeNode(arr[idx]);
    root->left = createTree(n, idx * 2 + 1, arr);
    root->right = createTree(n, idx * 2 + 2, arr);
    return root;
}

int main() {
    int n;
    std::cin >> n;
    int* arr = new int[n];
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    TreeNode* root = createTree(n, 0, arr);
    Solution sol;
    std::cout << (sol.isValidBST(root) ? "true" : "false") << std::endl;
    delete[] arr;
    return 0;
}