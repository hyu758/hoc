#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    cin>>s;
    string t="hello";
    int count=0;
    int j=0,i=0;
    while (i<s.size() && j<5){
    	if (s[i]==t[j]){
    		count++;
    		i++;
    		j++;
		}
		else{
			i++;
		}
	}
	if (count<5){
		cout<<"NO";
	}
	else{
		cout<<"YES";
	}
	
}
