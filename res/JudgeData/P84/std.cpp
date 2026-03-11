#include <iostream>
#include <vector>
#include <cstring>
using namespace std;
using ll = long long;

namespace Fusu {

const int maxt = 32;
const int maxn = 105;

int n, q, m;
ll a[maxn];

struct Mat {
  int x, y;
  ll mt[maxn][maxn];

  Mat(const int X = 0, const int Y = 0) : x(X), y(Y) {
    memset(mt, 0, sizeof(mt));
  }

  Mat operator*(const Mat &o) const {
    Mat ret(x, o.y);
    for (int i = 1; i <= x; ++i) {
      for (int j = 1; j <= o.y; ++j) {
        for (int k = 1; k <= y; ++k) {
          ret.mt[i][j] ^= mt[i][k] * o.mt[k][j];
        }
      }
    }
    return ret;
  }
};
Mat g[maxt], f;

void Main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> n >> m >> q;
  for (int i = 1; i <= n; ++i) cin >> a[i];
  g[0].x = g[0].y = n;
  for (int u, v; m; --m) {
    cin >> u >> v;
    g[0].mt[u][v] = g[0].mt[v][u] = 1;
  }
  for (int i = 1, di = i - 1; i < maxt; di = i++) {
    g[i] = g[di] * g[di];
  }
  for (ll x; q; --q) {
    cin >> x;
    f.x = 1; f.y = n;
    for (int i = 1; i <= n; ++i) f.mt[1][i] = a[i];
    for (ll w = 1, i = 0; w <= x; w <<= 1, ++i) {
      if (x & w) {
        f = f * g[i];
      }
    }
    cout << f.mt[1][1] << "\n";
  }
}

} // namespace Fusu

int main() {
  Fusu::Main();
  return 0;
}