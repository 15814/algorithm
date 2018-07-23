// 题目描述
// 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

class Solution {
public:
    int GetUglyNumber_Solution(int index) {
        if (index <= 0) {
            return 0;
        }
        if (index == 1) {
            return 1;
        }

        int* uglynumbers = new int[index+1];
        int nextidx = 1;
        uglynumbers[0] = 1;

        int* ugly2 = uglynumbers;
        int* ugly3 = uglynumbers;
        int* ugly5 = uglynumbers;
        while (nextidx < index) {
            int nextuglynumber = min(min(*ugly2*2,*ugly3*3),*ugly5*5);
            uglynumbers[nextidx] = nextuglynumber;
            while (*ugly2 * 2 <= nextuglynumber) {
                ugly2++;
            }
            while (*ugly3 * 3 <= nextuglynumber) {
                ugly3++;
            }
            while (*ugly5 * 5 <= nextuglynumber) {
                ugly5++;
            }
            nextidx++;
        }
        int result = uglynumbers[nextidx-1];
        delete[] uglynumbers;
        return result;

    }
};
