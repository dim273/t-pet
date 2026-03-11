#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

class BookQueue {
private:
    stack<int> inStack, outStack;
    void in2out() {
        while (!inStack.empty()) {
            outStack.push(inStack.top());
            inStack.pop();
        }
    }
public:
    BookQueue() {}
    void push(int bookID) {
        inStack.push(bookID);
    }
    int pop() {
        if (outStack.empty()) {
            if (inStack.empty()) {
                return -1;
            }
            in2out();
        }
        int value = outStack.top();
        outStack.pop();
        return value;
    }
};

int main() {
    string op;
    vector<string> operations;
    vector<vector<int>> values;
    vector<int> result;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> op;
        operations.push_back(op);
        if (op == "push") {
            int bookID;
            cin >> bookID;
            values.push_back({bookID});
        } else {
            values.push_back({});
        }
    }

    BookQueue bq;
    for (int i = 0; i < n; i++) {
        if (operations[i] == "push") {
            bq.push(values[i][0]);
        } else if (operations[i] == "pop") {
            result.push_back(bq.pop());
        }
    }

    for (int val : result) {
        cout << val << " ";
    }
    cout << endl;
    return 0;
}