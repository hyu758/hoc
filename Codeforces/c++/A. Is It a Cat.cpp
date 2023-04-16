#include <bits/stdc++.h>
using namespace std;
string upperCase(string s){
	for(int i = 0; i < s.size(); i++) {
    s.at(i) = toupper(s.at(i));
}
	return s;
}
void solve(){
	string s;
    string x="MEOW";
    int n;
	cin>>n;
	cin>>s;
	string tmp=upperCase(s);
	tmp.erase(unique(tmp.begin(), tmp.end()), tmp.end());
	if (tmp==x){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
}

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    
    while (t){
    	solve();
    	cout<<"\n";
    	t--;
	}
}
