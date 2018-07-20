

class Solution {
public:
    double Power(double base, int exponent) {
        if (base == 0) {
            return 0;
        }
        if (exponent == 0) {
            return 1;
        }
        unsigned int ex = abs(exponent);
        double ans = recur_power(base,ex);
        if (exponent < 0) {
            return 1.0/ans;
        }else{
            return ans;
        }
    }

    double recur_power(double base, unsigned int ex){
        if (ex == 0) {
            return 1;
        }
        if (ex == 1) {
            return base;
        }
        if (ex % 2 == 0) {
            return pow(recur_power(base,ex/2),2);
        }else{
            return pow(recur_power(base,ex/2),2) * base;
        }
    }
};


// note pow(x,y) is in header <cmath>
