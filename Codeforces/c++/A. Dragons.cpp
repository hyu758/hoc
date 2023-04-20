#include <bits/stdc++.h>
using namespace std;
void solve(int h,int m){
	int res=0;
	while (h<24){
		if (m<60){
			m++;
			res++;
		}
		else{
			m=0;
			h++;
		}
	}
	cout<<res<<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    short t;
    cin>>t;
    while (t--){
    	short h,m;
    	cin>>h>>m;
    	solve(h,m);
	}
    
}
