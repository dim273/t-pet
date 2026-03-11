#include <iostream>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int next[1000005];
    for (int i = 0; i < n; i++) {
        next[i] = i + 1;
    }
    next[n] = 1;
    int p = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j < m; j++) {
            p = next[p];
        }
        cout << next[p] << (i == n ? '\n' : ' ');
        next[p] = next[next[p]];
    }
    return 0;
}