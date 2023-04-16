#include <bits/stdc++.h>
using namespace std;
int charToInt(char x){
	return x-'0';
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    string s;
    cin>>t;
    while (t){
    	int res=0;
    	cin>>s;
		int tmp1=charToInt(s[0]);
		int tmp2=charToInt(s[2]);
    	cout<<tmp1+tmp2<<"\n";
    	t--;
	}
}
