#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n, m, ans, cnt = 1;
int f[40005];
int w[100005], v[100005];

int main() {
    int a, b, c;
    scanf("%d%d", &n, &m);

    for (int i = 1; i <= n; ++i) {
        scanf("%d%d%d", &a, &b, &c);
        for (int j = 1; j <= c; j <<= 1) {
            v[++cnt] = j * a;
            w[cnt] = j * b;
            c -= j;
        }
        if (c) {
            v[++cnt] = a * c;
            w[cnt] = b * c;
        }
    }

    for (int i = 1; i <= cnt; ++i)
        for (int j = m; j >= w[i]; --j)
            f[j] = max(f[j], f[j - w[i]] + v[i]);

    printf("%d\n", f[m]);
    return 0;
}