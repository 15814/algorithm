#include <iostream>
#include <vector>

using namespace std;

const unsigned int MAX = 100000+100;

int A[MAX]= {0};

int main(int argc, char const *argv[]) {

    int T;
    int n;
    std::cin >> T;
    while (T--) {
        std::cin >> n;
        int len = n;

        int i = 0;
        int tmp;
        while (n--) {
            cin>>tmp;
            A[i] = tmp;
            i++;
        }
        int sum = 0;
        int start = 0;
        int end = len-1;
        bool work = false;
        while (start < end) {
            while (A[start] < 1) {
                start++;
                if (start >= end) {
                    work = true;
                    break;
                }
            }
            if (work) {
                break;
            }
            while (A[end] < 1) {
                end--;
                if (start >= end) {
                    work = true;
                    break;
                }
            }
            if (work) {
                break;
            }

            if (start < end) {
                int levels = min(A[start],A[end]);
                if (levels > 0) {
                    sum += (end - start)*levels;
                    for (size_t i = start; i <= end; i++) {
                        A[i] -= levels;
                    }
                }
            }
        }
        cout<< sum <<endl;

    }

    return 0;
}






//
