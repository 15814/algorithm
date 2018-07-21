// 题目描述
// 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
// 输出描述:
// 对应每个测试案例，输出两个数，小的先输出。


class Solution {
public:
    vector<int> FindNumbersWithSum(vector<int> array,int sum) {

        std::vector<int> result;

        unsigned int sep = 0;
        while (sep < array.size() && array[sep] < sum) {
            ++sep;
        }

        int sep2 = 0;
        while (sep2 < array.size() && array[sep2] <= 0) {
            ++sep2;
        }

        for (size_t i = 0; i < sep2; i++) {
            for (size_t j = sep; j < array.size(); j++) {
                if (array[i] + array[j] >= sum) {
                    if (array[i] + array[j] == sum) {
                        result.push_back(array[i]);
                        result.push_back(array[j]);
                    }
                    break;
                }
            }
        }

        // [sep2,sep)
        for (size_t i = sep2; i < sep; i++) {
            for (size_t j = i+1; j < sep; j++) {
                if (array[i] + array[j] >= sum) {
                    if (array[i] + array[j] == sum) {
                        result.push_back(array[i]);
                        result.push_back(array[j]);
                    }
                    break;
                }
            }
        }



        if (result.size() <= 2) {
            return result;
        }else{
            int min_mutipy = result[0] * result[1];
            int minidx = 0;
            for (size_t i = 2; i < result.size()-1; i += 2) {
                int mutipy = result[i] * result[i+1];
                if (mutipy < min_mutipy) {
                    min_mutipy = mutipy;
                    minidx = i;
                }
            }
            int res1 = result[minidx], res2 = result[minidx+1];
            result.clear();
            result.push_back(res1);
            result.push_back(res2);

            return result;

        }

    }



















};
