#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
	int n,m;
	cin>>n>>m;
	int a[n];
	for (int x=0;x<n;x++){
		cin>>a[x];
	}
	int l=0;
	int sum=0,count=0;
	for (int r=0;r<n;r++){
		sum+=a[r];
		while (sum>=m){
			sum-=a[l];
			count+=n-r;
			l++;
		}
	}
	cout<<count;

	return 0;
}
