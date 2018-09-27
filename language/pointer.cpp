#include <iostream>
#include <vector>

using namespace std;

#ifndef MAXN
#define MAXN 10
#endif

int rt_array[MAXN];

int (*foo_rt_array())[MAXN]{
    // 返回一个指向包含10个int 的数组 指针    
    for (size_t i = 0; i < MAXN; i++) {
        rt_array[i] = i;
    }
    return &rt_array;
}

int main(int argc, char const *argv[]) {

    double *dp = nullptr;
    double *dp2 = dp;
    // *dp = a;
    //dp = &a;
    cout<< dp2 <<endl;
    cout<< dp <<endl;
    cout<< &dp <<endl;
    cout<< &dp2 <<endl;
    cout<< &dp2 - &dp <<endl;

    int val  = 1024;
    int *p   = &val;
    int **pp = &p;
    int ***ppp = &pp;
    int ****pppp = &ppp;

    printf("%d\n", ****pppp);
    // cout<< **pppp <<endl; //error
    int (*rp)[10] = foo_rt_array();


    for (size_t i = 0; i < MAXN; i++) {
        printf("%d %d %d\n",rt_array[i],(*rp)[i], *rp[i]); // notice the great diff between *rp[i] and (*rp)[i] in here
    }

    return 0;
}






//
