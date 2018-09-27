#include <iostream>
#include <vector>

using namespace std;

bool foo(int A,int B, int C)
{
 bool result = false;
 for(int m = 1; m <= B; m++)
 {
  if( (m * A) % B == C )
  {
   result = true;
   break;
  }
 }
 return result;
}

int main(int argc, char const *argv[]) {

    int n;
    std::cin >> n;
    int a,b,c;
    while (n--) {
        std::cin >> a>>b>>c;
        if (foo(a,b,c)) {
            cout<<"YES"<<endl;
        }else{
            cout<< "NO" <<endl;
        }
    }

    return 0;
}






//
