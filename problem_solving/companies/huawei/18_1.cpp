
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char const *argv[]) {

    int n;
    std::vector<double> vec;
    while (cin>>n) {
        for (size_t i = 0; i < n; i++) {
            double tmp;
            cin>>tmp;
            vec.push_back(tmp);
            /* code */
        }
        double sum = 0.0;
        double min=vec[0],max=vec[0];
        for (int i = 0; i < vec.size(); i++) {
            if(vec[i]>max) max = vec[i];
            if(vec[i]<min) min = vec[i];
            sum += vec[i];
        }
        sum = sum - min - max;
        double avg = sum/double(vec.size()-2);
        printf("%.2f\n",avg);
        vec.clear();
    }

    return 0;
}
