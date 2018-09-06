#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int const MAXCOL = 2100;
int const MAXROW = 2100;
int const COUNT_COL = 0;
int const COUNT_HIGH = 0;
int matrix[MAXROW][MAXCOL] = {0};

int main(int argc, char const *argv[]) {

    //vector<vector<int> > matrix(MAXROW);
    int n = 0;
    int m = 0;
    while (cin>>n) {
        //matrix.clear();
        for (size_t i = 0; i < MAXCOL; i++) {
            matrix[0][i] = 1;
            matrix[i][0] = 0;
        }

        if (n <= 0) {
            cout<< 0 <<endl;
            break;
        }else{
            int score = 0;
            cin>>m;
            int cols = n;
            int total = m;
            int col;
            for (size_t i = 0; i < m; i++) {
                cin >> col;
                if (col >=1 && matrix[0][col] < MAXROW) {
                    int insert_row =  matrix[0][col];
                    matrix[0][col]++;
                    ++matrix[insert_row][COUNT_COL];
                    if (matrix[insert_row][COUNT_COL] >= n) {
                        ++score;
                        // for (size_t i = 1; i <= cols; i++) {
                        //     --matrix[COUNT_HIGH][i];
                        // }
                        //matrix.erase(matrix.begin()+insert_row);

                    }
                }
            }
            cout<< score <<endl;
        }
    }
    return 0;
}














//
