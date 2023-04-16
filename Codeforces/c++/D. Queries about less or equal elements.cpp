#include <bits/stdc++.h>
using namespace std;
void solve(int a[], int b[], int n, int m){
	vector<pair<int,int>>p1;
	vector<pair<int,int>>p2;
	for (int i=0; i<m;i++){
		p1.push_back({b[i],i});
		p2.push_back({i,b[i]});
	}
	sort(p1.begin(),p1.end());
	for (int i=0; i<m;i++){
		p2[i].first=p1[i].second;
	}
	sort(b,b+m);
	int i=0,j=0;
	while (i<n && j<m){
		if (b[j]>=a[i]){
			i++;
		}
		else{
			p2[j].second=i;
			j++;
		}
	}
	while (j<m){
	    p2[j].second=i;
	    j++;
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
    for (int i=0;i<n;i++){
    	cin>>a[i];
	}
	for (int i=0;i<m;i++){
    	cin>>b[i];
	}
    sort(a,a+n);
    solve(a,b,n,m);
}
