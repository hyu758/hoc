#include <bits/stdc++.h>
using namespace std;
bool solve(string s,string t){
	for (auto x:s){
		for (auto z:t){
			if (x==z){
				return true;
			}
		}
	}
	return false;
}

int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    string t="HQ9";
    cin>>s;
    if (solve(s,t)){
    	cout<<"YES";
	}
	else{
		cout<<"NO";
	}
    
    
}
