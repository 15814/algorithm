#include <iostream>
#include <vector>

using namespace std;

bool is_huiwenshu(unsigned int number,unsigned int base,vector<int> &v);


int find_huiwenshu(int start){
    // base 2
    std::vector<int> vec2;
    std::vector<int> vec8;
    std::vector<int> vec10;

    start = max(start,10);
    unsigned int number = start;

    while (number > 0) {
        if (is_huiwenshu(number,2,vec2)&& is_huiwenshu(number,8,vec8) && is_huiwenshu(number,10,vec10)) {
            return number;
        }
        number++;
    }
    return -1;
}

bool is_huiwenshu(unsigned int number,unsigned int base,vector<int> &v){
    if (number == 0) {
        return true;
    }
    if (!v.empty()) {
        v.clear();
    }
    while (number > 0) {
        int remainder = number % base;
        v.push_back(remainder);
        number = number/base;
    }
    int end = v.size()-1;
    int start = 0;
    while (start < end) {
        if (v[start] != v[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

int main(int argc, char const *argv[]) {

    int result = find_huiwenshu(0);
    cout<< result <<endl;
    return 0;
}






//
