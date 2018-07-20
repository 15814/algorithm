

class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        int size = rotateArray.size();
        if (size <= 0) {
            return 0;
        }

        int start = 0;
        int end = size;
        int mid;
        int result = -1;

        while (end-start >= 1) {
            mid = start + ((end-start)>>1);
            if (mid+1 < end && rotateArray[mid] > rotateArray[mid+1]) {
                result = rotateArray[mid+1];
                break;
            }
            if (rotateArray[mid] > rotateArray[start]) {
                start = mid;
            }else{
                end = mid;
            }
        }

        if (result == -1) {
            int min = rotateArray[0];
            for (size_t i = 0; i < size; i++) {
                if (rotateArray[i] < min) {
                    min = rotateArray[i];
                }
            }
            result = min;
        }

        return result;


    }
};


















/*
AC notes:



*/
