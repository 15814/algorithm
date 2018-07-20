
// 神一样的解法 1，非常巧妙，想想篮球投篮时的，中+1分，不中-1分，然后看你最后分数的正负，就能看你的命中率是否大于50%，异曲同工。
class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {

        if (numbers.empty()) {
            return 0;
        }
        int number = numbers[0];
        int times = 0;
        for (size_t i = 0; i < numbers.size(); i++) {
            if (numbers[i] == number) {
                ++times;
            }else{
                --times;
                if (times < 0) {
                    number = numbers[i];
                    if(i != numbers.size()-1) times = 1;
                }
            }
        }
        if (times > 0) {
            return number;
        }else{
            return 0;
        }
    }
};


// 解法 2 主要是为了秀操作，寻找第 k（k=size/2) 大的数字，然后遍历一遍，如果他出现次数不大于 size/2,那么数组中不存在出现次数超过一半的数字，否则就是该 k大数字。


class Solution {
public:
    int MoreThanHalfNum_Solution(vector<int> numbers) {

        if (numbers.empty()) {
            return 0;
        }



    }

    int partation(std::vector<int> numbers, int number, int start, int end){

        for (int i = start; i < end; i++) {
            

        }
    }
};










// 解法3，借助 hashmap
