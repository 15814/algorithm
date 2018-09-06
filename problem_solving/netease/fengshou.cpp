#include <iostream>
#include <vector>

using namespace std;

const int SIZE = 10e5 + 100;
int apple[SIZE] = {0};

int main(int argc, char const *argv[]) {

    int n = 0;
    int m = 0;

    while (std::cin >> n) {
        int cursum = 0;
        for (int i = 0; i < n; i++) {
            int tmp;
            scanf("%d",&tmp);
            cursum += tmp;
            apple[i] = cursum;
        }

        m = 0;
        while (std::cin >> m) {
            while (m--) {
                int tofind = 0;
                scanf("%d",&tofind);
                for (int i = 0; i < n; i++) {
                    if (apple[i] >= tofind) {
                        printf("%d\n", i+1);
                        break;
                    }
                }
                int low = 0;
                int high = n;
                // for (int i = 0; i < n; i++) {
                //     printf("%d ", apple[i]);
                // }
                // printf("\n");
                // while (low <= high) {
                //     if (low == high) {
                //         printf("%d\n", low+1);
                //         break;
                //     }
                //
                //     int mid = low + ((high-low)>>1);
                //     if (apple[mid] == tofind) {
                //         printf("%d\n", mid+1);
                //         break;
                //     }
                //     if (apple[mid] > tofind) {
                //         high = mid;
                //     }else{
                //         low = mid+1;
                //     }
                    // printf("%d %d\n",low,high );
                // }
            }
        }
    }

    return 0;
}






//
