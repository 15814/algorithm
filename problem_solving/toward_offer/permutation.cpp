// 题目描述
// 输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
// 输入描述:
// 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。

#include <vector>
#include <string>
#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<string> Permutation(string str) {
        std::vector<string> result;
        set<string> setdic;

        if (str.empty()) {
            return result;
        }
        recur_permutation(str,0,result,setdic);
        sort(result.begin(),result.end());
        return result;
    }

    void recur_permutation(string str, int idx, vector<string> &result, set<string> &setdic){

        if (idx >= str.size()) {
            auto insert_return = setdic.insert(str);
            if (insert_return.second) {
                result.push_back(str);
            }
            //printf("%s\n", str.c_str());

        }

        for (size_t i = idx; i < str.size(); i++) {
            swap(str[idx],str[i]);
            recur_permutation(str,idx+1,result,setdic);
            swap(str[idx],str[i]);
        }

    }
};

int main(int argc, char const *argv[]) {
    Solution solution = Solution();
    string str = "abc";
    std::vector<string> result;
    result = solution.Permutation(str);
    for (size_t i = 0; i < result.size(); i++) {
        std::cout << result[i] << '\n';
    }
    return 0;
}
