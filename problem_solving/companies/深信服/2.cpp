#include <iostream>
#include <vector>
#include <cmath>
#include <float.h>
using namespace std;


int main(int argc, char const *argv[]) {

    int T;
    std::cin >> T;
    while (T--) {
        int a1,b1,v1,a2,b2,v2;
        std::cin >> a1>>b1>>v1>>a2>>b2>>v2;
        if (a1*b2 == b1*a2) {
            cout<< "UNKNOWN" <<endl;
            continue;
        }
        double d = a2*b1 - a1*b2;
        double x = double(b1*v2-b2*v1)/d;
        double y = double(v1*a2-v2*a1)/d;
        double eps = DBL_MIN;

        if(x> 0 && y >0 && x- floor(x) < eps && y - floor(y) < eps){
            cout<< int(x)<<' '<<int(y) <<endl;
        }else{
            cout<< "UNKNOWN" <<endl;
        }

    }

    return 0;
}






//
