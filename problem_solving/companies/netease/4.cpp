#include <iostream>
#include <cstring>

using namespace std;

bool judge(const int *a, const int *b, const int *c)
{
    int in = 0, out = 0, count = 0;
    for (int i = 1; i != 10002; ++i)
    {
        if (a[i] != b[i])
        {
            if (abs(a[i] - b[i]) < 2 && (out == 0 || in == 0))
            {
                if (a[i] < b[i])
                {
                    out++;
                }
                else if (a[i] > b[i])
                {
                    in++;
                }
            }
            else
            {
                return false;
            }
        }
        else if (a[i] == 1 && c[i] == 1)
        {
            return false;
        }
        else if (a[i] != 0)
        {
            ++count;
        }
    }
    if (in != out)
    {
        return false;
    }
    if (count != 1 && (in == 0 || out == 0))
    {
        return false;
    }
    return true;
}

int main(int argc, char *argv[])
{
    int T = 0;
    while (cin >> T)
    {
        for (int i = 0; i != T; ++i)
        {
            int in[10001] = {0}, out[10001] = {0}, ind[10001] = {0};
            memset(in,0, sizeof(in));
            memset(out,0, sizeof(in));
            memset(ind,0, sizeof(in));
            int N = 0;
            cin >> N;
            for (int j = 0; j != N; ++j)
            {
                int k = 0, l = 0;
                cin >> k >> l;
                ++in[k], ++out[l];
                if (k == l)
                {
                    ++ind[k];
                }
            }
            if (judge(in, out, ind))
            {
                cout << "yes" << endl;
            }
            else
            {
                cout << "no" << endl;
            }
        }
    }
    return 0;
}
