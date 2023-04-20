#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,n;
    int a[t];
    cin>>t>>n;
    int j=1;
    for (int i=1;i<=t;i+=2){
    	a[j]=i;
    	cout<<j<<" ";
    	j++;
    	
	}
	cout<<endl;
	for (int i=2;i<=t;i+=2){
    	a[j]=i;
    	j++;
		
	}
	for (int i=1;i<=t;i++){
    	cout<<a[i]<<" ";
	}
}
