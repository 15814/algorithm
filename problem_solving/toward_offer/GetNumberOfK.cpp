// 题目描述
// 统计一个数字在排序数组中出现的次数。


// 思路：用二分查找找到该数字，然后查看左右是否还有等于的

class Solution {
public:
    int GetNumberOfK(vector<int> data ,int k) {
        if (data.empty()) {
            return 0;
        }

        int start = 0;
        int end = data.size()-1;
        int mid;
        int found = -1;

        while (start <= end) {
            if (start == end) {
                found = start;
                break;
            }
            mid = start + ((end-start)>>1);
            if (data[mid] == k) {
                found = mid;
                break;
            }else if (data[mid] > k) {
                end = mid - 1;
            }else{
                start = mid + 1;
            }
        }

        if (found == -1) {
            return 0;
        }else{
            if (data[found] != k) {
                return 0;
            }else{
                int count = 1;
                int idx = found + 1;
                while (idx < data.size() && data[idx] == k) {
                    count++;
                    idx++;
                }
                idx = found - 1;
                while (idx >= 0 && data[idx] == k) {
                    count++;
                    idx--;
                }

                return count;
            }
        }


    }





};
