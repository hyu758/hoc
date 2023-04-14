#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    long long n,k;
    cin>>n;
    vector<int> v;
    int i=1;
    while (i<=n){
    	if (i%2!=0){
    		v.push_back(i);
		}
		i++;
	}
	i=2;
    while (i<=n){
    	if (i%2==0){
    		v.push_back(i);
		}
		i++;
	}
	
	for (auto x:v){
		cout<<x<<" ";
	}
	cout<<v[3];
}
