//
// 题目描述
// 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

// 注意用 partaion 的方法 不能同时保证奇数和奇数，偶数和偶数之间的相对位置不变

class Solution {
public:
    void reOrderArray(vector<int> &array) {
        if (array.empty()) {
            return;
        }
        std::vector<int> odd;
        std::vector<int> even;
        for (size_t i = 0; i < array.size(); i++) {
            if (array[i] % 2 == 0) {
                even.push_back(array[i]);
            }else{
                odd.push_back(array[i]);
            }
        }
        for (size_t i = 0; i < odd.size(); i++) {
            array[i] = odd[i];
        }
        unsigned int offset = odd.size();
        for (size_t i = 0; i < even.size(); i++) {
            array[i+offset] = even[i];
        }

        return;

    }
};
