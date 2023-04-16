#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,n;
    char c;
    
    int res;
    string s;
    cin>>t;
    s+=s;
    while (t){
    	int count=0;
    	int max=0;
    	cin>>n;
    	cin>>c;
    	cin>>s;
    	s+=s;
    	for (int i=0;i<s.size();i++){
    		if (s[i]==c){
    			count=0;
    			while (s[i]!='g' && i<s.size()){
    				count++;
    				i++;
				}
				if (count>max){
					max=count;
				}
			}
		}
		cout<<max<<"\n";
    	t--;
	}
}
