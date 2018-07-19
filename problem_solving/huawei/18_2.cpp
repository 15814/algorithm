
#include <iostream>

using namespace std;


int main(int argc, char const *argv[]) {

    int ans[4];
    int guess[4];
    int countA=0,countB=0;

    while (std::cin >> ans[0]>>ans[1]>>ans[2]>>ans[3]) {
        for (size_t i = 0; i < 4; i++) {
            cin>>guess[i];
        }
        for (size_t i = 0; i < 4; i++) {
            if (guess[i]==ans[i]) {
                countA++;
            }else{
                for (size_t j = 0; j < 4; j++) {
                    if (guess[i]==ans[j]) {
                        countB++;
                    }
                }
            }

        }
        cout <<countA<<'A'<<countB<<'B'<< '\n';

    }

    return 0;
}
