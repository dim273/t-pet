#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<cstring>
using namespace std;

int a[50][50], yi[20], xjay[50], xjiany[50];
int n, c = 0;

void out() {
    if (c < 3) {
        for (int i = 1; i <= n; i++) {
            for (int k = 1; k <= n; k++) {
                if (a[i][k] == 1) {
                    cout << k;
                    if (i < n) cout << " ";
                    break;
                }
            }
        }
        cout << endl;
    }
    c++;
}

void zhanlin(int x, int y) {
    a[x][y] = 1;
    yi[y] = 1;
    xjiany[x - y + n] = 1;
    xjay[x + y] = 1;
}

void fangqi(int x, int y) {
    a[x][y] = 0;
    yi[y] = 0;
    xjiany[x - y + n] = 0;
    xjay[x + y] = 0;
}

int isok(int x, int y) {
    if (a[x][y] == 0 && yi[y] == 0 && xjiany[x - y + n] == 0 && xjay[x + y] == 0)
        return 0;
    return 1;
}

void dfs(int x) {
    if (x == n + 1) {
        out();
    } else {
        for (int k = 1; k <= n; k++) {
            if (isok(x, k) == 0) {
                zhanlin(x, k);
                dfs(x + 1);
                fangqi(x, k);
            }
        }
    }
}

int main() {
    cin >> n;
    dfs(1);
    cout << c << endl;
    return 0;
}