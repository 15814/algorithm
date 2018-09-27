#include <string>
using namespace std;

void reverse(string& str, unsigned int start, unsigned int end);

void special_reverse(string &str){
    if (str.size()<=1) {
        return;
    }
    reverse(str,0,str.size()-1);
    int start = 0;
    int end = 0;
    for (size_t i = 0; i < str.size()-1; i++) {
        if (str[i]==' ') {
            end = i-1;
            reverse(str,start,end);
            start = i+1;
        }
    }
    return;
}

void reverse(string& str, unsigned int start, unsigned int end) {
    while (start < end) {
        swap(str[start],str[end]);
        start++;
        end--;
    }

}

int main(int argc, char const *argv[]) {
    std::string str = "I am a student.";
    special_reverse(str);
    printf("%s\n", str.c_str());
    std::string empty_str;
    special_reverse(empty_str);
    printf("%s\n", empty_str.c_str());
    return 0;
}
