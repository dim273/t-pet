#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <stack>
#include <climits>

using namespace std;

class MinStack {
    stack<int> x_stack;
    stack<int> min_stack;
public:
    MinStack() {
        min_stack.push(INT_MAX);
    }
    
    void push(int x) {
        x_stack.push(x);
        min_stack.push(min(min_stack.top(), x));
    }
    
    void pop() {
        x_stack.pop();
        min_stack.pop();
    }
    
    int top() {
        return x_stack.top();
    }
    
    int getMin() {
        return min_stack.top();
    }
};

vector<string> parseOps(string line) {
    line.erase(remove(line.begin(), line.end(), ' '), line.end());
    if (line.size() >= 2 && line.front() == '[' && line.back() == ']') {
        line = line.substr(1, line.size() - 2);
    }
    vector<string> ops;
    stringstream ss(line);
    string token;
    while (getline(ss, token, ',')) {
        if (!token.empty() && token.front() == '"' && token.back() == '"') {
            token = token.substr(1, token.size() - 2);
        }
        ops.push_back(token);
    }
    return ops;
}

vector<vector<int>> parseParams(string line) {
    vector<vector<int>> params;
    vector<int> current;
    string numStr;
    bool inArray = false;
    int depth = 0;

    for (char c : line) {
        if (c == '[') {
            depth++;
            if (depth == 2) {
                inArray = true;
                current.clear();
                numStr.clear();
            }
        } else if (c == ']') {
            if (depth == 2) {
                if (inArray) {
                    if (!numStr.empty()) {
                        current.push_back(stoi(numStr));
                        numStr.clear();
                    }
                    params.push_back(current);
                    inArray = false;
                }
            }
            depth--;
        } else if (c == '-' || (c >= '0' && c <= '9')) {
            if (inArray) {
                numStr += c;
            }
        } else if (c == ',') {
            if (inArray) {
                if (!numStr.empty()) {
                    current.push_back(stoi(numStr));
                    numStr.clear();
                }
            }
        }
    }

    return params;
}

int main() {
    string opsLine, paramsLine;
    if (!getline(cin, opsLine)) return 0;
    if (!getline(cin, paramsLine)) return 0;

    vector<string> ops = parseOps(opsLine);
    vector<vector<int>> params = parseParams(paramsLine);

    if (ops.size() != params.size()) {
        return 0;
    }

    MinStack* obj = nullptr;
    vector<string> results;

    for (int i = 0; i < ops.size(); i++) {
        string op = ops[i];
        vector<int>& param = params[i];
        if (op == "MinStack") {
            if (obj != nullptr) {
                delete obj;
            }
            obj = new MinStack();
            results.push_back("null");
        } else if (op == "push") {
            if (!param.empty()) {
                obj->push(param[0]);
            }
            results.push_back("null");
        } else if (op == "pop") {
            obj->pop();
            results.push_back("null");
        } else if (op == "top") {
            int t = obj->top();
            results.push_back(to_string(t));
        } else if (op == "getMin") {
            int m = obj->getMin();
            results.push_back(to_string(m));
        }
    }

    cout << "[";
    for (int i = 0; i < results.size(); i++) {
        if (i > 0) cout << ",";
        cout << results[i];
    }
    cout << "]" << endl;

    delete obj;
    return 0;
}