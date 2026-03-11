#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

const int maxn = 200005;
const double INF = 1e20;

int n, temp[maxn];
struct Point {
    double x, y;
} S[maxn];

bool cmp(const Point &a, const Point &b) {
    if (a.x < b.x) return true;
    if (a.x > b.x) return false;
    return a.y < b.y;
}

bool cmps(const int &a, const int &b) {
    return S[a].y < S[b].y;
}

double dist(int i, int j) {
    double dx = S[i].x - S[j].x;
    double dy = S[i].y - S[j].y;
    return sqrt(dx*dx + dy*dy);
}

double merge(int left, int right) {
    if (left == right) return INF;
    if (left + 1 == right) return dist(left, right);
    int mid = (left + right) / 2;
    double d1 = merge(left, mid);
    double d2 = merge(mid + 1, right);
    double d = min(d1, d2);
    int k = 0;
    for (int i = left; i <= right; ++i) {
        if (fabs(S[mid].x - S[i].x) < d) {
            temp[k++] = i;
        }
    }
    sort(temp, temp + k, cmps);
    for (int i = 0; i < k; ++i) {
        for (int j = i + 1; j < k && S[temp[j]].y - S[temp[i]].y < d; ++j) {
            double d3 = dist(temp[i], temp[j]);
            if (d3 < d) d = d3;
        }
    }
    return d;
}

int main() {
    scanf("%d", &n);
    for (int i = 0; i < n; ++i) {
        scanf("%lf%lf", &S[i].x, &S[i].y);
    }
    sort(S, S + n, cmp);
    double ans = merge(0, n - 1);
    printf("%.4lf\n", ans);
    return 0;
}