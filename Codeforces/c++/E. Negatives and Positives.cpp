#include <bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t,n;
    cin>>t;
    n=3;
    int count=0,sum;
    int a[t][n];
    for (int i=0;i<t;i++){
    	for (int j=0;j<n;j++){
    		cin>>a[i][j];
		}
	}
	for (int i=0;i<n;i++){
		sum=0;
		for (int j=0;j<t;j++){
			sum+=a[j][i];
		}
		if (sum==0){
			count++;
		}
	}

	if (count==3){
		cout<<"YES";
	}
	else{
		cout<<"NO";
	}
}
