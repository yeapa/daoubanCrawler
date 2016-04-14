#include <iostream>
using namespace std;
int main(int argc,char * argv[]){
  int n;
  int count=1;
  cin>>n;
  int ** a=new int* [n];
  for (int i = 0; i < n; i++) {
    a[i]=new int[n];
  }

  for (int  i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      a[i][j]=0;
    }
  }
  for (int k = 0; k < n-2; k++) {
    for (int j = k; j < n-k-1; j++) {
      a[k][j]=count++;
    }

    for (int i = k; i < n-k-1; i++) {
      a[i][n-k-1]=count++;
    }

    for (int j = n-k-1; j > k; j--) {
      a[n-k-1][j]=count++;
    }

    for (int i = n-k-1; i > k; i--) {
      a[i][k]=count++;
    }
  if (n%2==1) {
    a[(n-1)/2][(n-1)/2]=count;
  }

  }

  for (int  i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      cout<<a[i][j]<<'\t';
    }
    cout<<endl;
  }
  return 1;
}
