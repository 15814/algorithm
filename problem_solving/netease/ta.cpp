#include <iostream>

#include <vector>
#include <algorithm>
#include <utility>

using namespace std;


int main(int argc, char const *argv[]) {

    int n;
    int k;
    std::vector<int> v;
    std::vector<pair<int,int> > ops;

    while (std::cin >> n >> k) {
        const int size = n;
        int count = n;
        v.clear();
        ops.clear();

        while (count--) {
            int tmp;
            std::cin >> tmp;
            v.push_back(tmp);
        }
        int gap = 0;
        int operations = 0;
        while (operations < k) {
            auto result = std::minmax_element(v.begin(), v.end());

            gap = (*result.second) - (*result.first);
            if (gap == 0) {
                break;
            }
            *result.first += 1;
            *result.second -= 1;
            ops.push_back(make_pair((result.second-v.begin())+1, (result.first-v.begin())+1));
            operations++;
        }

        auto result = std::minmax_element(v.begin(), v.end());
        gap = (*result.second) - (*result.first);

        printf("%d %d\n", gap, operations);
        for (size_t i = 0; i < operations && i < ops.size(); i++) {
            printf("%d %d\n", ops[i].first, ops[i].second);
        }
        // for (size_t i = 0; i < v.size(); i++) {
        //     printf("%d\n", v[i]);
        // }
        // std::cout << "end a sample" << '\n';
    }


    return 0;
}






//
