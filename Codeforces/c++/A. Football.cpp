#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    string s;
    cin>>s;
    int i=0,j=1;
    int tmp=0;
    while (i<s.size() && j<s.size()){
    	if (tmp==7){
    		break;
		}
    	if (s[i]!=s[j]){
    		j++;
    		tmp+=1;
		}
		else{
			i=j-1;
			j++;
			tmp=0;
		}
	}
	if (tmp==7){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
}
