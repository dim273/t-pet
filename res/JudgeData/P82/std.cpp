#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <utility>
#include <vector>
#define N 524292
#define ll long long
#define reg register
#define p 998244353
using namespace std;

struct Z{
    int v;
    inline Z(const int _v=0):v(_v){}
};

inline Z operator + (const Z& lhs,const Z& rhs){ return lhs.v+rhs.v<p ? lhs.v+rhs.v : lhs.v+rhs.v-p; }
inline Z operator - (const Z& lhs,const Z& rhs){ return lhs.v<rhs.v ? lhs.v-rhs.v+p : lhs.v-rhs.v; }
inline Z operator - (const Z& x){ return x.v?p-x:0; }
inline Z operator * (const Z& lhs,const Z& rhs){ return (ll)lhs.v*rhs.v%p; }
inline Z& operator += (Z& lhs,const Z& rhs){ lhs.v = lhs.v+rhs.v<p ? lhs.v+rhs.v : lhs.v+rhs.v-p; return lhs; }
inline Z& operator -= (Z& lhs,const Z& rhs){ lhs.v = lhs.v<rhs.v ? lhs.v-rhs.v+p : lhs.v-rhs.v; return lhs; }
inline Z& operator *= (Z& lhs,const Z& rhs){ lhs.v = (ll)lhs.v*rhs.v%p; return lhs; }

template<typename T> inline void read(T& x){
    x = 0;
    char c = getchar();
    while(c<'0'||c>'9') c = getchar();
    while(c>='0'&&c<='9'){
        x = x*10+(c^48);
        c = getchar();
    }
}

inline Z power(Z a,int t){
    Z res = 1;
    while(t){
        if(t&1) res *= a;
        a *= a;
        t >>= 1;
    }
    return res;
}

int ms;

struct matrix{
    Z a[8][8];
    inline matrix(){ memset(a,0,sizeof(a)); }

    inline matrix operator * (const matrix& b) const{
        matrix res = matrix();
        for(reg int i=0;i!=ms;++i)
        for(reg int j=0;j!=ms;++j)
        for(reg int k=0;k!=ms;++k)
            res.a[i][j] += a[i][k]*b.a[k][j];
        return res;
    }
}I;

inline bool operator == (const matrix& lhs,const matrix& rhs){
    for(reg int i=0;i!=ms;++i)
    for(reg int j=0;j!=ms;++j)
        if(lhs.a[i][j].v!=rhs.a[i][j].v) return false;
    return true;
}

struct poly{
    Z a[9];
    int t;
    inline Z operator [] (const int& x) const{ return a[x]; }
    inline Z& operator [] (const int& x){ return a[x]; }

    inline Z eval(const int& x){
        Z res = a[t];
        for(reg int i=t-1;~i;--i) res = a[i]+res*x;
        return res;
    }
}P[9];

inline matrix getmat(int x){
    matrix res = matrix();
    Z p0 = P[0].eval(x+ms);
    for(reg int i=0;i!=ms-1;++i) res.a[i+1][i] = p0;
    for(reg int i=0;i!=ms;++i) res.a[i][ms-1] = -P[ms-i].eval(x+ms);
    return res;
}

Z fac[N],ifac[N],rt[N],facm[N],inv[N];
int rev[N];
int siz;

inline int getlen(int n){ return 1<<(32-__builtin_clz(n)); }

void init(int n){
    int lim = 1;
    while(lim<=n) lim <<= 1,++siz;
    for(reg int i=1;i!=lim;++i) rev[i] = (rev[i>>1]>>1)|((i&1)<<(siz-1));
    Z w = power(3,(p-1)>>siz);
    inv[1] = fac[0] = fac[1] = ifac[0] = ifac[1] = rt[lim>>1] = 1;
    for(reg int i=lim>>1|1;i!=lim;++i) rt[i] = rt[i-1]*w;
    for(reg int i=(lim>>1)-1;i;--i) rt[i] = rt[i<<1];
    for(reg int i=2;i<=n;++i) fac[i] = fac[i-1]*i;
    ifac[n] = power(fac[n],p-2);
    for(reg int i=n-1;i;--i) ifac[i] = ifac[i+1]*(i+1);
    for(reg int i=2;i<=n;++i) inv[i] = fac[i-1]*ifac[i];
    for(reg int i=0;i!=ms;++i) I.a[i][i] = 1;
}

inline void dft(Z *f,int lim){
    static unsigned long long a[N];
    reg int x,shift = siz-__builtin_ctz(lim);
    for(reg int i=0;i!=lim;++i) a[rev[i]>>shift] = f[i].v;
    for(reg int mid=1;mid!=lim;mid<<=1)
    for(reg int j=0;j!=lim;j+=(mid<<1))
    for(reg int k=0;k!=mid;++k){
        x = a[j|k|mid]*rt[mid|k].v%p;
        a[j|k|mid] = a[j|k]+p-x;
        a[j|k] += x;
    }
    for(reg int i=0;i!=lim;++i) f[i] = a[i]%p;
}

inline void idft(Z *f,int lim){
    reverse(f+1,f+lim);
    dft(f,lim);
    reg int x = p-((p-1)>>__builtin_ctz(lim));
    for(reg int i=0;i!=lim;++i) f[i] *= x;
}

inline void lagrange(const matrix* F1,const Z *F2,int n,Z m,matrix* R1,Z *R2,bool flag){
    static Z pre[N],suf[N],f1[N],f2[N],g[N],inv_[N],ifcm[N],mul;
    int k = n<<1|1,lim = getlen(n<<1);
    facm[0] = 1;
    for(reg int i=0;i<=n;++i){
        facm[0] *= m-n+i;
        ifcm[i] = ifac[i]*ifac[n-i];
    }
    pre[0] = suf[k+1] = 1;
    for(reg int i=1;i<=k;++i) pre[i] = pre[i-1]*(m-n+i-1);
    for(reg int i=k;i;--i) suf[i] = suf[i+1]*(m-n+i-1);
    mul = power(pre[k],p-2);
    for(reg int i=1;i<=k;++i) inv_[i] = mul*pre[i-1]*suf[i+1];
    for(reg int i=1;i<=n;++i) facm[i] = facm[i-1]*(m+i)*inv_[i];
    for(reg int i=0;i!=k;++i) g[i] = inv_[i+1];
    memset(g+k,0,(lim-k+1)<<2);
    dft(g,lim);
    for(reg int i=0;i<=n;++i) f2[i] = ifcm[i]*((n-i)&1?-F2[i]:F2[i]);
    memset(f2+n+1,0,(lim-n)<<2);
    dft(f2,lim);
    for(reg int i=0;i!=lim;++i) f2[i] *= g[i];
    idft(f2,lim);
    for(reg int i=0;i<=n;++i) R2[i] = f2[i+n]*facm[i];
    if(!flag) return;
    for(reg int i=0;i!=ms;++i)
    for(reg int j=0;j!=ms;++j){
        for(reg int t=0;t<=n;++t) f1[t] = ifcm[t]*((n-t)&1?-F1[t].a[i][j]:F1[t].a[i][j]);
        memset(f1+n+1,0,(lim-n)<<2);
        dft(f1,lim);
        for(reg int t=0;t!=lim;++t) f1[t] *= g[t];
        idft(f1,lim);
        for(reg int t=0;t<=n;++t) R1[t].a[i][j] = f1[t+n]*facm[t];
    }
}

inline matrix ff(int d,int x){
    matrix res = getmat(x);
    for(reg int i=1;i!=d;++i) res = res*getmat(x+i);
    return res;
}

inline Z gg(int d,int x){
    Z res = P[0].eval(x);
    for(reg int i=1;i!=d;++i) res *= P[0].eval(x+i);
    return res;
}

int k;

pair<matrix,Z> magic(int s,int t){
    static Z g[N],gd[N],invs = power(s,p-2);
    static matrix f[N],fd[N];
    static int st[30],top = 0,x = s,d = 1,kd;
    while(x){
        st[++top] = x;
        x >>= 1;
    }
    for(reg int i=0;i<=k;++i){
        x = i*s;
        g[i] = P[0].eval(x);
        f[i] = getmat(x);
    }
    --top;
    while(top--){
        kd = k*d;
        lagrange(f,g,kd,kd+1,f+kd+1,g+kd+1,true);
        g[kd<<1|1] = 0;
        f[kd<<1|1] = matrix();
        lagrange(f,g,kd<<1,d*invs,fd,gd,true);
        for(reg int i=0;i<=(kd<<1);++i){
            f[i] = f[i]*fd[i];
            g[i] *= gd[i];
        }
        d <<= 1;
        if(!(st[top+1]&1)) continue;
        kd = k*(d+1);
        for(reg int i=k*d+1;i<=kd;++i){
            x = i*s;
            f[i] = ff(d,x),g[i] = gg(d,x);
        }
        for(reg int i=0;i<=kd;++i){
            x = i*s;
            f[i] = f[i]*getmat(x+d);
            g[i] *= P[0].eval(x+d);
        }
        ++d;
    }
    lagrange(f,g,k*s,ms*invs,f,g,false);
    matrix r1 = I;
    Z r2 = 1;
    for(reg int i=0;i<=t;++i) r1 = r1*f[i],r2 *= g[i];
    return make_pair(r1,r2);
}

Z P_recursive(const Z *a,int n){
    int tn = n-ms+1,s;
    s = ceil(sqrt(tn*1.0/k))+1;
    pair<matrix,Z> tmp = magic(s,(tn-s)/s);
    matrix mul = tmp.first;
    Z div_ = tmp.second,res = 0;
    for(reg int i=(tn/s)*s;i!=tn;++i){
        mul = mul*getmat(i);
        div_ *= P[0].eval(i+ms);
    }
    for(reg int i=0;i!=ms;++i) res += a[i]*mul.a[i][ms-1];
    return res*power(div_,p-2);
}

int n;
Z a[9];

int main(){
    read(n),read(ms),read(k);
    init(262147);
    for(reg int i=0;i!=ms;++i) read(a[i]);
    for(reg int i=0;i<=ms;++i){
        P[i].t = k;
        for(reg int j=0;j<=k;++j) read(P[i][j]);
    }
    Z ans = P_recursive(a,n);
    printf("%d",ans.v);
    return 0;
}