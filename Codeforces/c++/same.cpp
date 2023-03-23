#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int n,m;
	cin>>n>>m;
	int a[n],b[m];
	
	for (int x=0;x<n;x++){
		cin>>a[x];
	}
	for (int x=0;x<m;x++){
		cin>>b[x];
	}
	int i=0,j=0;
	int ans=0,c1=0,c2=0;
	while (i < n && j< m){
		if (a[i]<b[j]){
			i++;
			continue;
		}
		else if (a[i]>b[j]){
			j++;
			continue;
		}
		while (a[i]==b[j]){
			c1++;
			i++;
		}
		i--;
		while (b[j]==a[i]){
			c2++;
			j++;
		}
	ans+=c1*c2;
	}
	cout<<ans;
 
	return 0;
}
