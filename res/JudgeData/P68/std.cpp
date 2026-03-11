#include <bits/stdc++.h>
using namespace std;

int main() {
    int n, k;
    cin >> n >> k;
    const int MAX_VAL = 30000;
    bool to[MAX_VAL + 1] = {false};
    for (int i = 0; i < n; ++i) {
        int x;
        cin >> x;
        if (x >= 1 && x <= MAX_VAL) {
            to[x] = true;
        }
    }
    int t = 0;
    for (int i = 1; i <= MAX_VAL; ++i) {
        if (to[i]) {
            ++t;
            if (t == k) {
                cout << i << endl;
                return 0;
            }
        }
    }
    cout << "NO RESULT" << endl;
    return 0;
}