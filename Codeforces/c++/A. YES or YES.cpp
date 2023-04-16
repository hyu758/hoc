#include <bits/stdc++.h>
using namespace std;
string upperCase(string s){
	for(int i = 0; i < s.size(); i++) {
    s.at(i) = toupper(s.at(i));
}
	return s;
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    string s;
    string x="YES";
    cin>>t;
    while (t){
    	cin>>s;

    	if (upperCase(s)==x){
    		cout<<"YES";
		}
		else{
			cout<<"NO";
		}
		cout<<"\n";
    	t--;
	}
}
