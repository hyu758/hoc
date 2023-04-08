#include <bits/stdc++.h>
using namespace std;
void solve(int a[], int b[], int n, int m){
	vector<pair<int,int>>p1;
	vector<pair<int,int>>p2;
	for (int i=1; i<=n;i++){
		p1.push_back({b[i],i});
		p2.push_back({i,b[i]});
	}
	sort(p1.begin(),p1.end());
	for (int i=1; i<=n;i++){
		p2[i].first=p1[i].second;
	}
	sort(b+1,b+m+1);
	int i=1,j=1;
	while (i<=n && j<=m){
		if (b[j]>=a[i]){
			i++;
		}
		else{
			p2[j].second=i;
// 			cout<<i-1<<" ";
			j++;
		}
	}
	sort(p2.begin(),p2.end());
	for (auto x:p2){
		cout<<x.second<<" ";
	}
}
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,m;
    cin>>n>>m;
    int a[n],b[m];
    for (int i=1;i<=n;i++){
    	cin>>a[i];
	}
	for (int i=1;i<=m;i++){
    	cin>>b[i];
	}
    sort(a+1,a+n+1);
    solve(a,b,n,m);
}
