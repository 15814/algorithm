#include <iostream>

using namespace std;

class Zerobase {

};

class Abase {
private:
    /* data */

public:
    Abase ();
    virtual ~Abase ();
};
class Bbase
{
    int a;
    char p;
};

class CBase
{
public:
    CBase(void);
    virtual ~CBase(void);
private:
    int  a;
    char *p;
};

class Dbase {
private:
    int  a;
    char *p;

public:
    Dbase ();
    //virtual ~Dbase ();
};

int main(int argc, char const *argv[]) {

    printf("sizeof(int): %lu\n", sizeof(int(1)));
    printf("sizeof Zerobase is %lu\n", sizeof(Zerobase));
    printf("sizeof Abase is %lu\n", sizeof(Abase));
    printf("sizeof Bbase is %lu\n", sizeof(Bbase));
    printf("sizeof CBase is %lu\n", sizeof(CBase));
    printf("sizeof Dbase is %lu\n", sizeof(Dbase));
    char* sp;
    int *p;
    long lg;
    printf("sizeof(int*p) %lu\n", sizeof(p));
    printf("sizeof(char*p) %lu\n", sizeof(sp));
    printf("sizeof(long) %lu\n", sizeof(lg));
    int a = 1>2?1:2;
    printf("%d\n", a);

    return 0;
}






//
