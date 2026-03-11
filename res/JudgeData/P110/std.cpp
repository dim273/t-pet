#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

class ListNode {
public:
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class MyLinkedList {
public:
    MyLinkedList() {
        size = 0;
        head = new ListNode(0);
    }

    int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        ListNode *cur = head;
        for (int i = 0; i <= index; i++) {
            cur = cur->next;
        }
        return cur->val;
    }

    void addAtHead(int val) {
        addAtIndex(0, val);
    }

    void addAtTail(int val) {
        addAtIndex(size, val);
    }

    void addAtIndex(int index, int val) {
        if (index > size) {
            return;
        }
        index = max(0, index);
        size++;
        ListNode *pred = head;
        for (int i = 0; i < index; i++) {
            pred = pred->next;
        }
        ListNode *toAdd = new ListNode(val);
        toAdd->next = pred->next;
        pred->next = toAdd;
    }

    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        size--;
        ListNode *pred = head;
        for (int i = 0; i < index; i++) {
            pred = pred->next;
        }
        ListNode *p = pred->next;
        pred->next = pred->next->next;
        delete p;
    }

private:
    int size;
    ListNode *head;
};

int main() {
    int n;
    cin >> n;
    vector<string> ops(n);
    for (int i = 0; i < n; i++) {
        cin >> ops[i];
    }
    MyLinkedList* list = new MyLinkedList();
    for (int i = 0; i < n; i++) {
        if (ops[i] == "addAtHead") {
            int val; cin >> val;
            list->addAtHead(val);
        } else if (ops[i] == "addAtTail") {
            int val; cin >> val;
            list->addAtTail(val);
        } else if (ops[i] == "addAtIndex") {
            int index, val;
            cin >> index >> val;
            list->addAtIndex(index, val);
        } else if (ops[i] == "get") {
            int index; cin >> index;
            cout << list->get(index) << "\n";
        } else if (ops[i] == "deleteAtIndex") {
            int index; cin >> index;
            list->deleteAtIndex(index);
        }
    }
    return 0;
}