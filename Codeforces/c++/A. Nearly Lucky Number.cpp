#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    cin>>s;
    s.erase(unique(s.begin(),s.end()),s.end());
    int count=0;
    for (int i=0;i<s.size();i++){
//    	if (s[i]=='4' || s[i]=='7'){
//    		count++;
//		}
//		else{
//			break;
//		}
		cout<<s[i]<<" ";
	}
	if (count==s.size()){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
}
