#include <iostream>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>

using namespace std;

int tobase10(int base, string s){
    int exp = 0;
    int result = 0;
    for (int i = s.size()-1; i >= 0; i--) {
        int tmp = s[i]-'0';
        if (tmp > 9) {
            tmp = s[i]-('A'-10);
        }
        result += tmp * pow(base,exp);
        exp++;
    }
    return result;
}

int main(int argc, char const *argv[]) {

    int n;
    std::cin >> n;
    //cout<< tobase10(13,"A") <<endl;

    while (n--) {
        int basex,basey;
        string s = "";
        std::cin >> basex >>basey >> s;

        int len = s.size();

        int k2 = double(len)/(1+log(double(basey))/log(double(basex)) );
        int k1 = len - k2;

        std::string s1 = s.substr(0,k1);
        std::string s2 = s.substr(k1);

        int value1 = tobase10(basex,s1);
        int value2 = tobase10(basey,s2);

        if (value1 == value2) {
            cout<< value1 <<endl;
        }else{
            while (value1 != value2) {
                if (value1 > value2) {
                    k1--;
                }else{
                    k1++;
                }
                if (k1 < 1 || k1 > s.size()-1) {
                    srand((unsigned)time(NULL));
                    k1 = (rand() % s.size())+ 1;
                }

                value1 = tobase10(basex,s.substr(0,k1));
                value2 = tobase10(basey,s.substr(k1));
                //printf("%d %d\n", value1, value2);
            }
            cout<< value1 <<endl;
        }

    }




    return 0;
}






//
