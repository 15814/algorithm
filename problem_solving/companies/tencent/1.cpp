#include <iostream>
#include <vector>
#include <stdio.h>

using namespace std;

# define MAXN 100000

int a[MAXN];


int gcd(int a ,int b)
{
	int temp;
	if(a<b)
	{
		temp=a;
		a=b;
		b=temp;
	}
	while(1)
	{ temp = a %b;
	if(!temp) break;
	  a =b ;
	  b =temp;
	}
	return b;
}
int lcm(int a,int b)
{
	int result =a *b /gcd(a,b);
	return result;
}

int lcmRow(int a[],int len)
{
    int i=0,temp;
	while(i<len-1)
	{
		temp=lcm(a[i],a[i+1]);
		i++;
		a[i]=temp;
	}
	return temp;
}


int main(int argc, char const *argv[]) {

    int n ;

    int size = 0;
    int m = 1;
    while (std::cin >> n) {
        if (n == 1) {
            cout<< 2 <<endl;
            continue;
        }
        if (n == 2) {
            cout<< 4 <<endl;
            continue;
        }
        int i ;
        for (i = 0; i <= n-2; i++) {
            a[i] = i + 2;
        }
        size = i;
        for (size_t i = 0; i < size; i++) {
            std::cout << a[i] << ' ';
        }
        m = lcmRow(a,size);
        cout<< m <<endl;
    }

    return 0;
}






//
