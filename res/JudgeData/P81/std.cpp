#include<bits/stdc++.h>
using namespace std;
const int _=2e6+10;
const int mod=998244353,g=3;
char ch;int T,ans,N;
int n,k,m,nn,n_,x,y,res,wn,v;
int n1,len;int invn,w;
int a[_],b[_],nt[_],suf[_];
int rev[_],inv[_],fac[_],ifac[_];
inline void read(int &x){
	x=0;ch=getchar();while(ch<47)ch=getchar();
	while(ch>47)x=(x<<1)+(x<<3)+(ch^48),ch=getchar();
}
void write(int x){if(x>9)write(x/10);putchar(48|x%10);}
inline void swap(int &x,int &y){x^=y^=x^=y;}
void qpow(int x,int k){
	res=1;
	while(k){
		if(k&1)res=1ll*res*x%mod;
		x=1ll*x*x%mod;k>>=1;
	}
}
void getinv(int n){
	register int i;
	for(inv[1]=1,i=2;i^n;++i)inv[i]=1ll*(mod-mod/i)*inv[mod%i]%mod;
}
void getinv(int n,int *f,int *g){
	static int i;
	for(suf[n]=1,i=n-1;~i;--i)suf[i]=1ll*suf[i+1]*f[i]%mod;
	qpow(suf[0],mod-2);g[0]=res;
	for(i=0;i^n;++i)g[i+1]=1ll*g[i]*f[i]%mod;
	for(i=0;i^n;++i)g[i]=1ll*g[i]*suf[i+1]%mod;
}
void getfac(int n){
	register int i;
	for(ifac[0]=1,i=1;i^n;++i)ifac[i]=1ll*ifac[i-1]*inv[i]%mod;
	for(fac[0]=1,i=1;i^n;++i)fac[i]=1ll*fac[i-1]*i%mod;
}
void getrev(int n){
	static int i;
	n1=1;len=-1;while(n1<(n<<1))n1<<=1,++len;
	for(i=0;i^n1;++i)rev[i]=(rev[i>>1]>>1)|((i&1)<<len);
}
void ntt_init(int n){
	register int i,mid,j;n<<=1;
	for(mid=1;mid<n;mid<<=1){
		qpow(g,(mod-1)/(mid<<1));
		wn=res;nt[mid]=1;j=(mid<<1);
		for(i=mid+1;i<j;++i)nt[i]=1ll*nt[i-1]*wn%mod;
	}
}
inline void reverse(int *a,int n){
	static int i,nn;nn=n>>1;
	for(i=0;i^nn;++i)swap(a[i],a[n-i-1]);
}
inline int add(int x,int y){return x+y>mod?x+y-mod:x+y;}
inline int sub(int x,int y){return x>y?x-y:x-y+mod;}
void ntt(int n,int *a,bool t){
	static int i,mid,j,k;
	for(i=0;i^n;++i)if(i<rev[i])swap(a[i],a[rev[i]]);
	for(mid=1;mid<n;mid<<=1){
		for(j=0;j<n;j+=(mid<<1)){
			for(k=0;k<mid;++k){
				x=a[j+k],y=1ll*nt[mid+k]*a[j+k+mid]%mod;
				a[j+k]=add(x,y);
				a[j+k+mid]=sub(x,y);
			}
		}
	}
	if(t){
		reverse(a+1,n-1);
		for(invn=inv[n],i=0;i^n;++i)a[i]=1ll*a[i]*invn%mod;
	}
}
int wrk[_],wrk_[_],trn[_];
void pre_trans(int n,int m){
	static int i;
	for(i=0;i^nn;++i)wrk[i]=i+m-n;
	getinv(nn,wrk,wrk_);
	for(i=0;i^nn;++i)wrk[i]=wrk_[i];
	for(i=nn+1;i^n1;++i)wrk[i]=0;ntt(n1,wrk,0);
	for(w=1,i=0;i<=n;++i)w=1ll*w*(m-i)%mod;trn[0]=w;
	for(i=1;i<=n;++i)trn[i]=1ll*trn[i-1]*(m+i)%mod*wrk_[i-1]%mod;
}
void trans_from(int n,int *f){
	static int i;
	for(i=0;i<=n;++i)f[i]=1ll*f[i]*ifac[i]%mod;
	for(i=0;i<=n;++i)f[i]=1ll*f[i]*(n-i&1?mod-ifac[n-i]:ifac[n-i])%mod;
	for(i=n+1;i^n1;++i)f[i]=0;ntt(n1,f,0);
}
void trans_to(int n,int *f,int *g){
	static int i;
	for(i=0;i^n1;++i)g[i]=1ll*f[i]*wrk[i]%mod;
	ntt(n1,g,1);for(i=0;i<=n;++i)g[i]=g[n+i];
	for(i=0;i<=n;++i)g[i]=1ll*g[i]*trn[i]%mod;
}
void trans_to(int n,int *f){
	static int i;
	for(i=0;i^n1;++i)f[i]=1ll*f[i]*wrk[i]%mod;
	ntt(n1,f,1);for(i=0;i<=n;++i)f[i]=f[n+i];
	for(i=0;i<=n;++i)f[i]=1ll*f[i]*trn[i]%mod;
}
int p[_],pp[_],q[_],qq[_],s[_],ss[_];
int tp[_],tpp[_],tq[_],tqq[_],ts[_],tss[_];
void iterate(int n){
	static int i,m;
	nn=(n<<1)+1,getrev(nn);
	m=1ll*n*inv[v]%mod;pre_trans(n,m);
	for(i=0;i<=n;++i)ss[i]=ts[i]=s[i];
	for(i=0;i<=n;++i)pp[i]=tp[i]=p[i];
	for(i=0;i<=n;++i)qq[i]=tq[i]=q[i];
	trans_from(n,s),trans_to(n,s,tss);
	trans_from(n,p),trans_to(n,p,tpp);
	trans_from(n,q),trans_to(n,q,tqq);
	for(i=0;i<=n;++i)ss[i]=tss[i];
	for(i=0;i<=n;++i)pp[i]=tpp[i];
	for(i=0;i<=n;++i)qq[i]=tqq[i];
	m=n+1;pre_trans(n,m);
	trans_to(n,s);trans_from(n,ss);trans_to(n,ss);
	trans_to(n,p);trans_from(n,pp);trans_to(n,pp);
	trans_to(n,q);trans_from(n,qq);trans_to(n,qq);
	for(i=0;i^n;++i)s[n+i+1]=s[i],ss[n+i+1]=ss[i];
	for(i=0;i^n;++i)p[n+i+1]=p[i],pp[n+i+1]=pp[i];
	for(i=0;i^n;++i)q[n+i+1]=q[i],qq[n+i+1]=qq[i];
	for(i=0;i<=n;++i)s[i]=ts[i],ss[i]=tss[i];
	for(i=0;i<=n;++i)p[i]=tp[i],pp[i]=tpp[i];
	for(i=0;i<=n;++i)q[i]=tq[i],qq[i]=tqq[i];
	n<<=1;
	for(i=0;i<=n;++i)s[i]=add(1ll*s[i]*pp[i]%mod,1ll*q[i]*ss[i]%mod);
	for(i=0;i<=n;++i)p[i]=1ll*p[i]*pp[i]%mod;
	for(i=0;i<=n;++i)q[i]=1ll*q[i]*qq[i]%mod;
}
void shift(int n){
	static int i;
	for(i=0;i^n;++i)s[i]=1ll*add(s[i],q[i])*(n+i*v)%mod;
	for(i=0;i^n;++i)p[i]=1ll*p[i]*(n+i*v)%mod;
	nn=N-n+1;for(i=0;i^n;++i)q[i]=1ll*q[i]*(nn-i*v)%mod;
	for(nn=n*v,w=1,i=n;i;--i)w=1ll*w*(nn+i)%mod,ss[i]=w;p[n]=w;
	for(nn=N-nn,w=1,i=1;i<=n;++i)ts[i]=w,w=1ll*w*(nn-i+1)%mod;q[n]=w;
	for(w=0,i=1;i<=n;++i)w=add(w,1ll*ss[i]*ts[i]%mod);s[n]=w;
}
void solve(int n){
	if(n==1){
		s[0]=1,s[1]=v+1;
		p[0]=1,p[1]=v+1;
		q[0]=N,q[1]=N-v;
	}
	else {
		solve(n>>1);iterate(n>>1);
		if(n&1)shift(n);
	}
}
inline int min(int a,int b){return a<b?a:b;}
inline int max(int a,int b){return a>b?a:b;}
int inqn[110],inqm[110];bool inqb;
main(){
	read(T);
	register int i,facm,mn;
	for(i=0;i^T;++i)read(inqn[i]),read(inqm[i]),nn=max(nn,inqm[i]);
	v=1;while(v*v+v<=nn)++v;--v;
	getinv(v<<4);ntt_init(v<<2);getfac(v<<1);
	for(int zt=0;zt^T;++zt){
		N=inqn[zt],m=inqm[zt];inqb=0;
		if(m>=N){qpow(2,N);write(res);putchar('\n');continue;}
		if(N==1){write(m+1);putchar('\n');continue;}
		if(N-m-1<m)inqb=1,m=N-m-1;
		if(m==0)ans=1;
		else if(m==1)ans=N+1;
		else if(m==2)ans=add(N+1,1ll*N*(N-1)%mod*inv[2]%mod);
		else {
			v=1;while(v*v+v<m)++v;--v;
			solve(v);nn=v*v+v;
			for(w=1,i=nn+1;i<=m;++i)w=1ll*w*i%mod;p[v+1]=w;
			for(mn=1,i=nn;i^m;++i)mn=1ll*mn*(N-i)%mod;
			for(i=v;~i;--i)p[i]=1ll*p[i]*p[i+1]%mod;
			facm=p[0];for(i=0;i<=v;++i)p[i]=p[i+1];
			for(i=1;i<=v;++i)q[i]=1ll*q[i-1]*q[i]%mod;
			mn=1ll*mn*q[v]%mod;for(i=v+1;i;--i)q[i]=q[i-1];q[0]=1;
			for(i=0;i<=v;++i)ans=add(ans,1ll*p[i]%mod*q[i]%mod*s[i]%mod);
			ans=add(ans,mn);nn=m-nn;
			for(i=0;i^nn;++i)ss[i]=N-(m-i-1);getinv(nn,ss,ts);
			for(i=0;i^nn;++i)mn=1ll*mn*ts[i]%mod*(m-i)%mod,ans=add(ans,mn);
			qpow(facm,mod-2);ans=1ll*ans*res%mod;
		}
		if(inqb)qpow(2,N),ans=sub(res,ans);
		write(ans);putchar('\n');ans=0;
	}
}
