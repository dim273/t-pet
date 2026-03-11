#include <iostream>
#include <algorithm>
#include <queue>
#include <string>
#include <vector>
#include <sstream>

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
    int maxDepth(TreeNode* root) {
        if (root == nullptr) return 0;
        return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};

// Helper function to build tree from level order input
// LeetCode style: [3,9,20,null,null,15,7]
TreeNode* buildTree() {
    string line;
    if (!getline(cin, line) || line.empty()) return nullptr;
    
    // Remove brackets if present
    if (line.front() == '[') line = line.substr(1);
    if (line.back() == ']') line.pop_back();
    
    stringstream ss(line);
    string item;
    vector<string> parts;
    while (getline(ss, item, ',')) {
        // Trim spaces
        item.erase(0, item.find_first_not_of(" \t\r\n"));
        item.erase(item.find_last_not_of(" \t\r\n") + 1);
        parts.push_back(item);
    }
    
    if (parts.empty() || parts[0] == "null" || parts[0].empty()) return nullptr;
    
    TreeNode* root = new TreeNode(stoi(parts[0]));
    queue<TreeNode*> q;
    q.push(root);
    
    int i = 1;
    while (!q.empty() && i < parts.size()) {
        TreeNode* curr = q.front();
        q.pop();
        
        // Left child
        if (i < parts.size()) {
            if (parts[i] != "null") {
                curr->left = new TreeNode(stoi(parts[i]));
                q.push(curr->left);
            }
            i++;
        }
        
        // Right child
        if (i < parts.size()) {
            if (parts[i] != "null") {
                curr->right = new TreeNode(stoi(parts[i]));
                q.push(curr->right);
            }
            i++;
        }
    }
    
    return root;
}

int main() {
    TreeNode* root = buildTree();
    Solution sol;
    cout << sol.maxDepth(root) << endl;
    return 0;
}
