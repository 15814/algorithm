#include <iostream>
#include <vector>
#include <string>

using namespace std;

void foo(char* out,const string& keyName,uint32_t uid=1) {
    printf("hellp foo\n");
}

struct A{
   unsigned int a;
   char b[2];
   double c;
   short d;
};

int main(int argc, char const *argv[]) {

    int n = 1;
    char* out = "hello";
    // *out += char(n-'0');
    //out += n;
    char* newout = new char[10];
    sprintf(newout, "%s%d",out, n);
    cout<< newout <<endl;

    char filename[3]={'a','b','c'};
    const string str = "hellp";
    foo(filename,str);

    A a_struct = A();
    printf("sizeof(a_struct) %lu\n", sizeof(a_struct));

    return 0;
}


void c_recipe1() {
    //在字符串后面添加数字变成一个新的字符串或者将一个字符串分割为多个的代码
    char oldString[10] = "circle|";
    char newString[10];
    int suffix = 3;

    sprintf(newString, "%s%d",oldString, suffix);

    printf("%s\n",newString);
    sscanf(newString,"%s%d",oldString,&suffix);
    printf("%s,%d",oldString,suffix);

}



//
