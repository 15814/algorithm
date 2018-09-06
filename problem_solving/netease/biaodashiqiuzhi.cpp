#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char const *argv[]) {

    int a,b,c;
    while (cin >> a >> b >> c) {
        int result1 = a + b + c;
        int result2 = a*b*c;
        int result3 = (a+b)*c;
        int result4 = a*(b+c);
        cout<< max(max(result1,result2),max(result3,result4))<<endl;
    }

    return 0;
}






//
