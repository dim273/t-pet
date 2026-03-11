#include <cstdio>
#include <vector>
using namespace std;

int main() {
    int V, n;
    scanf("%d %d", &V, &n);
    vector<int> w(n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &w[i]);
    }
    vector<int> f(V + 1, 0);
    for (int i = 0; i < n; i++) {
        for (int j = V; j >= w[i]; j--) {
            if (f[j] < f[j - w[i]] + w[i]) {
                f[j] = f[j - w[i]] + w[i];
            }
        }
    }
    printf("%d\n", V - f[V]);
    return 0;
}