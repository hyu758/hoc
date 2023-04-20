#include <bits/stdc++.h>
using namespace std;
void solve(){
	int n,k;
	cin>>n>>k;
	string s;
	cin>>s;
	int res=0;
	int tmp;
	int i=0,j=0;
    map<char,int> low,up;
    for (auto x:s){
    	if (x>=97){
    		low[x]++;
		}
		else{
			up[x+32]++;
		}
	}
	for (auto i='a';i<='z';i++){
		res+=min(low[i],up[i]);
		tmp=(abs(low[i]-up[i]))/2;
		res+=min(k,tmp);
		k-=min(k,tmp);
	}
	cout<<res<<"\n";
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while (t--){
    	solve();
		}
	}
