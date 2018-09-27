#include <iostream>
#include <vector>
#include <string>
using namespace std;


int main(int argc, char const *argv[]) {

    int n;
    string s;
    string result;
    std::cin >> n;

    while (n--) {
        s = "";
        result = "";
        std::cin >> s;
        int count = 0;
        int start = 0;

        for (size_t i = 0; i < s.size(); ) {

            if (i+1 < s.size() && s[i+1]-s[i] == 1) {
                start = i;
                //count++;
                int k = 2;
                while (i+k < s.size() && s[i+k]-s[i] == k) {
                    //count++;
                    k++;
                }
                int end = i+k;
                if (k >= 4) {
                    // result += s[start] + "-" + s[end-1];
                    result.push_back(s[start]);
                    result.push_back('-');
                    result.push_back(s[end-1]);
                }else{
                    result += s.substr(start,k);
                }
                //count = 0;
                i = end;
            }else{
                result += s[i];
                i++;
            }
        }

        cout<< result <<endl;

    }

    return 0;
}






//
