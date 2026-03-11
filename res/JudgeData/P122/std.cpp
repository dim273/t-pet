#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;

inline int read(){
    int res=0,f=1;char ch=' ';
    while(!isdigit(ch)){if(ch=='-') f=-1;ch=getchar();}
    while(isdigit(ch)){res=res*10+ch-'0';ch=getchar();}
    return res*f;
}
void write(int x){
    if(x<0){putchar('-');x=-x;}
    if(x>9) write(x/10);
    putchar(x%10+'0');
}
int max(int a,int b){
    return a>b?a:b;
}
const int N=1e5+5;
int n,m,T,dp[N],a,b,c,v,w,d;

void zeroone(int cost,int weight,int V){
    for(register int i=V;i>=cost;i--)
        dp[i]=max(dp[i],dp[i-cost]+weight);
}

void complete(int cost,int weight,int V){
    for(register int i=cost;i<=V;i++)
        dp[i]=max(dp[i],dp[i-cost]+weight);
}

void mutil(int cost,int weight,int num,int V){
    if(cost*num>=V){
        complete(cost,weight,V);
        return;
    }
    for(register int i=1;i<=num;i*=2){
        zeroone(i*cost,i*weight,V);
        num-=i;
    }
    if(num)zeroone(num*cost,num*weight,V);
}

int main()
{
    n=read(),m=read(),T=read();
    for(register int i=1;i<=n;i++)
        v=read(),w=read(),d=read(),mutil(v,w,d,T);
    for(register int i=1;i<=m;i++){
        a=read(),b=read(),c=read();
        for(register int j=T;j>=0;j--)
            for(register int u=0;u<=j;u++)
                dp[j]=max(dp[j],dp[j-u]+a*u*u+b*u+c);
    }
    write(dp[T]);
    return 0;
}