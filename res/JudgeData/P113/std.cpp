#include <bits/stdc++.h>

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if (l1 == nullptr) {
            return l2;
        } else if (l2 == nullptr) {
            return l1;
        } else if (l1->val < l2->val) {
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        } else {
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};

// Helper function to create a linked list from a vector
ListNode* createList(const std::vector<int>& nums) {
    ListNode* head = nullptr;
    ListNode* tail = nullptr;
    for (int num : nums) {
        ListNode* node = new ListNode(num);
        if (head == nullptr) {
            head = node;
            tail = node;
        } else {
            tail->next = node;
            tail = node;
        }
    }
    return head;
}

// Helper function to print a linked list
void printList(ListNode* head) {
    ListNode* curr = head;
    while (curr) {
        std::cout << curr->val;
        if (curr->next) std::cout << " ";
        curr = curr->next;
    }
    std::cout << std::endl;
}

int main() {
    int n1, n2;
    std::cin >> n1;
    std::vector<int> list1(n1);
    for (int i = 0; i < n1; i++) {
        std::cin >> list1[i];
    }
    std::cin >> n2;
    std::vector<int> list2(n2);
    for (int i = 0; i < n2; i++) {
        std::cin >> list2[i];
    }

    ListNode* l1 = createList(list1);
    ListNode* l2 = createList(list2);

    Solution solution;
    ListNode* merged = solution.mergeTwoLists(l1, l2);

    printList(merged);

    return 0;
}