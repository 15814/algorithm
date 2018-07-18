
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[]) {
    /* code */
    int n,m;

    while (cin>>n>>m) {
        std::vector<int> vec;
        vec.push_back(0);
        for (size_t i = 0; i < n; i++) {
            /* code */
            int tmp;
            cin>>tmp;
            vec.push_back(tmp);
        }
        while (m--) {
            char ch;
            int a,b;
            cin>>ch>>a>>b;

            if (ch=='Q') {
                if (a > b) {
                    swap(a,b);
                }
                int max = vec[a];
                for (int i = a; i <= b; i++) {
                    if (vec[i]>max) {
                        max = vec[i];
                        /* code */
                    }
                }
                std::cout << max << '\n';
                /* code */
            }
            if (ch=='U') {
                vec[a] = b;
                /* code */
            }
        }
    }
    return 0;
}
