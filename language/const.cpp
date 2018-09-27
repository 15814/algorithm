#include <iostream>
#include <vector>

using namespace std;

class Base{
public:
    int public_int;
    void change(){
        count++;
    }
    Base():public_int(0),count(0){
        static_int++;
        for (size_t i = 0; i < 5; i++) {
            a[i] = i;
        }
    }
    int getCount() const{
        return count;
    }
    int get_staticint()const{
        return static_int;
    }
private:
    // static int static_int = 1;
    // non-const static data member must be initialized out of line
    int count;
    static int static_int;
    const int const_int;
    int a[5];
};
int Base::static_int = 0;
const int Base::const_int = 0;

void test_pa(const int *pa) {
    cout<< *pa+1 <<endl;
    pa = nullptr;
    // *pa = 9; //error
}

void test_pa2(int * const pa) {
    cout<< *pa+1 <<endl;
    *pa = 9;
    // pa = nullptr; //error

}

void test_pbase(const Base* pbase) {
     pbase->getCount(); //error
}

int main(int argc, char const *argv[]) {
    Base base = Base();
    //printf("%d\n", base.getCount());
    Base *pbase = &base;
    base.public_int = 1;
    printf("%d\n", base.get_staticint());
    // test_pbase(pbase);
    //p->change();
    // cout<< sizeof(pbase) <<endl;

    const Base base2 = Base();
    printf("%d\n", base2.get_staticint());


    int a[5]{1,2,3,4,5};
    int *pa = a;
    int b = 1;
    int *pb = &b;
    // test_pa(pb);

    if (pb == nullptr) {
        cout<< "pb is nullptr" <<endl;
    }

    if (pa == a) {
        std::cout << "pa not change" << '\n';
    }

    //int * const pconst = a;
    

    return 0;
}






//
