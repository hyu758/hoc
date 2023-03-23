#include <bits/stdc++.h>
#include <string>
using namespace std;
 
int main(){
	ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n,m;
    cin >>n>>m;
    int a[n];
    int b[m];
    int res[m];
    int temp=0;
    int count=0;
	for (int i=0;i<n;i++){
		cin>>a[i];
	}
	for (int i=0;i<m;i++){
		cin>>b[i];
	}
	for (int i=0;i<m;i++){
		for (int j=temp;j<n;j++){
			if (b[i]>a[j]){
				count+=1;
			}
			else{
				temp=j;
				res[i]=count;
				
				break;
			}
		}
	}
	for (int i=0;i<m;i++){
		cout<<res[i]<<" ";
	}   
	return 0;
}
