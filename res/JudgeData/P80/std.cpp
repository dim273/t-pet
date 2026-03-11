#include <bits/stdc++.h>

typedef long long LL;
typedef unsigned long long ULL;

const int N = 131072;

int mod, mod_g, factor[N], ifactor[N];

void reduce(int &x) { x += x >> 31 & mod; }
int pow(int x, int y, int ans = 1) {
	for (; y; y >>= 1, x = (LL) x * x % mod)
		if (y & 1) ans = (LL) ans * x % mod;
	return ans;
}

void init(int n) {
	factor[0] = 1;
	for (int i = 1; i <= n; ++i)
		factor[i] = (LL) factor[i - 1] * i % mod;
	ifactor[n] = pow(factor[n], mod - 2);
	for (int i = n; i; --i)
		ifactor[i - 1] = (LL) ifactor[i] * i % mod;
}

int wn[N], w[N], lim, s, rev[N];
void fftinit(int len) {
	wn[0] = lim = 1, s = -1; while (lim < len) lim <<= 1, ++s;
	for (int i = 1; i < lim; ++i) rev[i] = rev[i >> 1] >> 1 | (i & 1) << s;
	const int w = pow(mod_g, (mod - 1) / lim);
	for (int i = 1; i < lim; ++i) wn[i] = (LL) wn[i - 1] * w % mod;
}
void fft(int *A, int typ) {
	static ULL tmp[N];
	for (int i = 0; i < lim; ++i) tmp[rev[i]] = A[i];
	for (int i = 1; i < lim; i <<= 1) {
		for (int j = 0, t = lim / i / 2; j < i; ++j) w[j] = wn[j * t];
		for (int j = 0; j < lim; j += i << 1)
			for (int k = 0; k < i; ++k) {
				const ULL x = tmp[k + j + i] * w[k] % mod;
				tmp[k + j + i] = tmp[k + j] + mod - x, tmp[k + j] += x;
			}
	}
	for (int i = 0; i < lim; ++i) A[i] = tmp[i] % mod;
	if (!typ) {
		const int il = pow(lim, mod - 2); std::reverse(A + 1, A + lim);
		for (int i = 0; i < lim; ++i) A[i] = (LL) A[i] * il % mod;
	}
}

void clear(int *a) { std::memset(a, 0, lim << 2); }
void copy(int *a, int *b, int n) { std::memcpy(a, b, n + 1 << 2); }
void multiply(int *a, int *b, int *c) {
	fft(a, 1), fft(b, 1);
	for (int i = 0; i < lim; ++i) c[i] = (LL) a[i] * b[i] % mod;
	fft(c, 0);
}
void poly_shift(int *f, int n, int *g, int k) {
	static int a[N], b[N], q[N]; fftinit(n + n + 1), clear(a), clear(b);
	for (int i = 0; i <= n; ++i) a[i] = (LL) f[i] * ifactor[i] % mod * ifactor[n - i] % mod;
	for (int i = n - 1; i >= 0; i -= 2) a[i] = mod - a[i];

	b[0] = k - n;
	for (int i = 1; i <= 2 * n; ++i) b[i] = (LL) b[i - 1] * (k + i - n) % mod;
	q[2 * n] = pow(b[2 * n], mod - 2);
	for (int i = 2 * n; i; --i) q[i - 1] = (LL) q[i] * (k + i - n) % mod;
	for (int i = 2 * n; i; --i) b[i] = (LL) q[i] * b[i - 1] % mod; b[0] = q[0];

	multiply(a, b, a);
	static int suf[N], isuf[N]; suf[2 * n + 1] = 1;
	for (int i = 2 * n; ~i; --i)
		suf[i] = (LL) suf[i + 1] * (i + k - n) % mod;
	isuf[0] = pow(suf[0], mod - 2);
	for (int i = 0; i <= 2 * n; ++i)
		isuf[i + 1] = (LL) isuf[i] * (i + k - n) % mod;
	for (int i = 0; i <= n; ++i) {
		if ((i + k) % mod <= n) g[i] = f[(i + k) % mod];
		else g[i] = (LL) isuf[i + n + 1] * a[i + n] % mod * suf[i] % mod;
	}
}

int n, size, f[N], g[N];

void boom(int n) {
	static int a[N], b[N], c[N], d[N];
	poly_shift(f, n, a, n + 1);
	for (int i = 1; i <= n; ++i) f[n + i] = a[i - 1];
	poly_shift(f, 2 * n, b, pow(size, mod - 2, n));
	poly_shift(g, n, c, n + 1);
	for (int i = 1; i <= n; ++i) g[n + i] = c[i - 1];
	poly_shift(g, 2 * n, d, pow(size, mod - 2, n));
	for (int i = 0; i <= 2 * n; ++i) {
		g[i] = ((LL) g[i] * b[i] + (LL) d[i] * f[i]) % mod;
		f[i] = (LL) f[i] * b[i] % mod;
	}
}
void qaq(int n) {
	f[n + 1] = g[n + 1] = 1;
	int tmp = 1, x = (n + 1) * size % mod;
	for (int i = 1; i <= n; ++i)
		f[n + 1] = (LL) f[n + 1] * (x + i) % mod;
	for (int i = 2; i <= n; ++i) {
		tmp = tmp * (x + i - 1LL) % mod;
		g[n + 1] = ((LL) g[n + 1] * (x + i) + tmp) % mod;
	}
	for (int i = 0; i <= n + 1; ++i) {
		x = (LL) i * size % mod;
		g[i] = (g[i] * (x + n + 1LL) + f[i]) % mod;
		f[i] = f[i] * (x + n + 1LL) % mod;
	}
}

void solve(int n) {
	if (n == 1) {f[1] = size + 1, f[0] = g[0] = g[1] = 1; return;}
	solve(n >> 1), boom(n >> 1); if (n & 1) qaq(n - 1);
}

int solve() {
	if (!n) return 0; int ans = 0;
	size = std::sqrt(n), init(size), solve(size);
	int x = 0, y = 1;
	for (int i = 0; i < size; ++i)
		x = ((LL) f[i] * x + (LL) y * g[i]) % mod, y = (LL) y * f[i] % mod;
	for (int i = size * size + 1; i <= n; ++i)
		x = ((LL) i * x + y) % mod, y = (LL) i * y % mod;
	return pow(y, mod - 2, x);
}

void test() {
	std::cin >> n >> mod >> mod_g, n = std::min(n, mod - n - 1);
	std::cout << solve() << '\n';
}

int main() {
	std::ios::sync_with_stdio(0), std::cin.tie(0);
	int tc; std::cin >> tc; while (tc--) test();
	return 0;
}