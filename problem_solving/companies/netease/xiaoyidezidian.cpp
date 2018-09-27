#include <iostream>
#include <vector>
#include <string>

using namespace std;

const int M = 10007;
const int MAXN = 101;
int C[MAXN+1][MAXN+1];
void Initial()
{
int i,j;
for(i=0; i<=MAXN; ++i)
{
C[0][i] = 0;
C[i][0] = 1;
}
for(i=1; i<=MAXN; ++i)
{
for(j=1; j<=MAXN; ++j)
// C[i][j] = (C[i-1][j] + C[i-1][j-1]) % M;
C[i][j] = (C[i-1][j] + C[i-1][j-1]);
}
}

int combination(int n, int m)
{
return C[n][m];
}

string generate(int n, int m, int k, string result){
    
    return result;
}

int main(int argc, char const *argv[]) {
    Initial();
    //cout<< combination(4,2) <<endl;
    int n,m,k;

    while (std::cin >> n >> m >> k) {
        if (k > combination(n+m,min(n,m))) {
            printf("%d\n", -1);
            continue;
        }

        int count_a = n;
        int count_z = m;
        string result = "";

        generate(n,m,k,result);



        // while (k != 0) {
        //     if (k & 1) {
        //         result += "z";
        //         count_z--;
        //     }else{
        //         result += "a";
        //         count_a--;
        //     }
        //     // if (count_a <= 0 || count_z <= 0) {
        //     //     break;
        //     // }
        //     k = (k>>1);
        // }
        // if (count_a >= 0 && count_z >= 0) {
        //     int diff_len = n+m - result.size();
        //     for (int i = 0; i < diff_len; i++) {
        //         cout<< 'a';
        //     }
        //     for (int i = 0; i < result.size(); i++) {
        //         cout<< result[i];
        //     }
        //     cout<<endl;
        // }else{
        //     cout<< -1 <<endl;
        // }
    }

    return 0;
}






//
