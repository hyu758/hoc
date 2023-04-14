#include <bits/stdc++.h>
using namespace std;
void solve(){
	int n;
	cin>>n;
	string s;
	cin>>s;
	int ans=n;
	int l=0,r=n-1;
	while (s[l]!=s[r] && ans>0){
		l++;
		r--;
		ans-=2;
	}
	cout<<ans<<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while (t>0){
    	solve();
    	t--;
	}
}
