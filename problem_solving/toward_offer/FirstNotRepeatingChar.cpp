

// 在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.



class Solution {
public:
    int FirstNotRepeatingChar(string str) {
        if (str.size() == 0) {
            return -1;
        }
        if (str.size() == 1) {
            return 0;
        }

        int const DICT_LEN = 512;
        int dict[DICT_LEN];
        for (size_t i = 0; i < DICT_LEN; i++) {
            dict[i] = -2;
        }

        for (size_t i = 0; i < str.size(); i++) {
            int idx = int(str[i]);
            if (dict[idx] == -2) {
                dict[idx] = i;
            }else if (dict[idx] >= 0) {
                dict[idx] = -1;
            }
        }

        unsigned int minidx = str.size();
        bool found = false;
        for (size_t i = 0; i < DICT_LEN; i++) {
            if (dict[i] >= 0 && dict[i] < minidx) {
                minidx = dict[i];
                found = true;
            }
        }
        if (found) {
            return minidx;
        }else{
            return -1;
        }

    }
};
























//
