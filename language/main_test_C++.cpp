#include <iostream>
#include <vector>

#include "play.h"

using namespace std;

int MAXLEN = 10;

void test_static() {
    static int count = 0;
    count++;
    printf("%d\n", count);

}

void test_const() {
    const int a = 1;
    const int b = 2;
    int c = 3;
    int const *p1 = &a; //指针指向为常量
    int* const p2 = &c; //指针本身是常量
    p1 = &b; // ok
    //p2 = &b;  // error
}

int main(int argc, char const *argv[]) {




    return 0;
}






//
