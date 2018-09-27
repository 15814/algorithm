#include <iostream>
#include <vector>

using namespace std;


int main(int argc, char const *argv[]) {

    char s;
    std::vector<int> v;
    int tmp;
    cin>>tmp;
        v.clear();
        v.push_back(tmp);
        while (cin>>s>>tmp) {
            v.push_back(tmp);
        }
        int len = v.size();
        int totalsum = 0;
        for (size_t i = 0; i < len; i++) {
            totalsum += v[i];
        }
        int cursum = 0;
        bool work = false;
        int result = 0;
        for (size_t i = 0; i < len; i++) {
            cursum += v[i];
            if (cursum-v[i] == totalsum - cursum) {
                result = v[i];
                work = true;
                break;
            }
        }
        if (work) {
            printf("%d\n", result);
        }else{
            printf("False\n");
        }

    return 0;
}






//
