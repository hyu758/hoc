#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin>>n;
    int a[n];
    int res=0;
    for (int i=0;i<n;i++){
		cin>>a[i];
		}
    int max;
	sort(a,a+n);
	for (int i=0;i<n-1;i++){
		res+=a[n-1]-a[i];
	}
	cout<<res;
}
