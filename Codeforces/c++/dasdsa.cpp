#include <bits/stdc++.h>
using namespace std;
void solve(){
	int n;
	cin>>n;
	int a[n],b[n];
	for (int i=0;i<n;i++){
		cin>>a[i];
	}
	for (int i=0;i<n;i++){
		cin>>b[i];
	}
	int i=0,j=0,res=0;
	while (i<n){
		while (i>=j){
			if (a[i]!=b[j]){
				j++;
		}
			else{
				i++;
				res+=1;
			}
		}
		i++;
		j=0;
	}
	cout<<res<<"\n";
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
}
