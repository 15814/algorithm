#include <iostream>
#include <vector>

using namespace std;

struct SA {
int i;

SA() {}
};

#include <assert.h>
#include <stddef.h> // for NULL

class A {public: virtual void f();};
class B {public: virtual void g();};
class AB: public virtual A, public B {};

// void simple_dynamic_casts()
// {
//   AB ab;
//   B* bp = &ab;        // no casts needed
//   A* ap = &ab;
//   AB& abr = dynamic_cast<AB&>(*bp);  // succeeds
//   ap = dynamic_cast<A*>(bp);         assert(ap!= NULL);
//   bp = dynamic_cast<B*>(ap);         assert(bp!= NULL);
//   ap = dynamic_cast<A*>(&abr);       assert(ap!= NULL);
//   bp = dynamic_cast<B*>(&abr);       assert(bp!= NULL);
// }


int main(int argc, char const *argv[]) {

    const SA ra;
    // ra.i = 10; //直接修改const类型，编译错误
    SA &rb = const_cast<SA&>(ra);
    //SA *rb = const_cast<SA&>(ra);
    rb.i =10;
    printf("%d\n", ra.i);

    int n = 6;
    int *p1 = &n;
    //double *d = static_cast<double*>(p1);
    double d = static_cast<double>(n);
    void *p = static_cast<void*>(p1);
    p = &d;
    // cout<< *p  <<endl; //error
    // printf("%f\n", *p); // error 不能输出 void 指针

    double d2 = reinterpret_cast<double &>(n);
    printf("%lf\n", d2);
    int n2 = reinterpret_cast<int &>(d2);
    printf("%d\n", n2);
    //simple_dynamic_casts();

    int a = 1;
    double dd = 2.1;
    cout<< a + dd <<endl;
    cout<< "f+a: " << dd+a <<endl;
    printf("%lf\n", dd+a);
    a = d;
    cout<< "a = f: " << (a = dd )<<endl;

    int &ref  = a;
    cout<< "ref: " << ref <<endl;
    ref = n;
    cout<< "ref: " << ref <<endl;

    return 0;
}






//
