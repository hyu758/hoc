#include <bits/stdc++.h>
using namespace std;
void solve(){
	string s;
    cin>>s;
    set<char> v;
    for (int i=0;i<s.size();i++){
    	if (s[i]==s[i+1]){
    		i++;
		}
		else{
			v.insert(s[i]);
		}
		}
    	for (auto x: v){
    		cout<<x;
		}
		cout<<"\n";
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
	return 0;
}