#include <iostream>
#include <vector>

using namespace std;

int const MAX = 100000+100;
int weight[MAX] = {0};


int main(int argc, char const *argv[]) {

    int n,k;

    while (cin>>n>>k) {
        int sum = 0;
        int const K = k;
        int const N = n;

        for (size_t i = 0; i < N; i++) {
            cin >> weight[i];
        }
        for (size_t i = 0; i < N; i++) {
            int work;
            std::cin >> work;
            if (work == 1) {
                sum += weight[i];
                weight[i] = 0;
            }
        }

        int max_ksum = 0;
        int pre_ksum = 0;
        for (size_t i = 0; i < K; i++) {
            pre_ksum += weight[i];
        }
        max_ksum = pre_ksum;

        for (size_t i = 0; i < N && i+K < N; i++) {
            int currentsum = pre_ksum + weight[i+K] - weight[i];
            if (currentsum > max_ksum) {
                max_ksum = currentsum;
            }
            pre_ksum = currentsum;
        }
        sum += max_ksum;
        cout<< sum <<endl;

    }

    return 0;
}



















//
