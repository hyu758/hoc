#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    while (t>0){
    	int n,s;
    	cin>>n>>s;
    	int a[n];
    	int l=1;
    	int sum=0;
    	for (int i=1;i<=n;i++){
    		cin>>a[i];
		}
		int f=1;
		while (f){
			for (int i=l;i<=n;i++){
				cout<<a[i]<<endl;
				cout<<sum<<endl;
				}
			if (sum+s<0){
				l++;
			}
			else{
				f=0;
				cout<<l<<" ";
				cout<<r<<endl;
			}
		}
		t--;
	}
	return 0;
}
