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
	int count=0;
	while (i < n && j< m){
		if (b[j]==a[i]){
			count+=1;
			j++;
		}
		else if (b[j]>a[i]){
			i++;
		}
		else{
			j++;
		}
	}
	cout<<count;
 
	return 0;
}
