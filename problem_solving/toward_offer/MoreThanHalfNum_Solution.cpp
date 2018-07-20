

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
