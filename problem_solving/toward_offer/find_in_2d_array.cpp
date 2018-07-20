

class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        if (array.size() == 0) {
            return false;
        }
        int rows = array.size();
        int cols = array[0].size();

        if (rows == 1 && cols == 1) {
            return (target == array[0][0]);
        }

        return recur_find(target,array,rows,cols,0,cols-1);

    }

    bool recur_find(int target, vector<vector<int> > array, int rows, int cols, int row, int col){

        if (row > rows-1 || col < 0) {
            return false;
        }

        if (target == array[row][col]) {
            return true;
        }else if (target < array[row][col]) {
            col--;
        }else{
            row++;
        }
        return recur_find(target,array,rows,cols,row,col);
    }
};
