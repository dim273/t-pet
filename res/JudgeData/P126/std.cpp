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
    void inorder(TreeNode* root, vector<int>& res) {
        if (!root) {
            return;
        }
        inorder(root->left, res);
        res.push_back(root->val);
        inorder(root->right, res);
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        inorder(root, res);
        return res;
    }
};

TreeNode* buildTree(const vector<int>& arr, int idx) {
    if (idx >= arr.size() || arr[idx] == -1) {
        return nullptr;
    }
    TreeNode* node = new TreeNode(arr[idx]);
    node->left = buildTree(arr, 2 * idx + 1);
    node->right = buildTree(arr, 2 * idx + 2);
    return node;
}

int main() {
    vector<int> arr;
    int x;
    while (cin >> x) {
        arr.push_back(x);
    }
    if (arr.empty()) {
        cout << "[]";
        return 0;
    }
    TreeNode* root = buildTree(arr, 0);
    Solution sol;
    vector<int> res = sol.inorderTraversal(root);
    cout << "[";
    for (size_t i = 0; i < res.size(); ++i) {
        cout << res[i];
        if (i + 1 < res.size()) cout << ",";
    }
    cout << "]";
    return 0;
}