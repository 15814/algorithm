#include <iostream>

class Solution {
public:
    bool isNumeric(char* string)
    {
        if (string == NULL || string[0] == '\0') {
            return false;
        }
        bool state = true;

        char* cur = string;
        if (*cur == '+' || *cur == '-' || (int(*cur)-int('0') >=0 && int(*cur)-int('0') <= 9)) {
            if (*cur == '+' || *cur == '-') {
                cur++;
                state = false;
            }

            while (*cur != '\0' && int(*cur)-int('0') >=0 && int(*cur)-int('0') <= 9) {
                cur++;
                state = true;
            }
            if (*cur == '\0') {
                return state;
            }
            if (*cur == '.' || *cur == 'E' || *cur == 'e') {
                if (*cur == '.') {
                    cur++;
                    state = !state;
                    while (*cur != '\0' && int(*cur)-int('0') >=0 && int(*cur)-int('0') <= 9) {
                        cur++;
                        state = true;
                    }
                    if (*cur == '\0' || !state) {
                        return state;
                    }
                }
                if (*cur == 'E' || *cur == 'e') {
                    cur++;
                    state = false;
                    if (*cur != '\0' && (*cur == '+' || *cur == '-')) cur++;
                    while (*cur != '\0' && int(*cur)-int('0') >=0 && int(*cur)-int('0') <= 9) {
                        cur++;
                        state = true;
                    }
                    if (*cur != '\0') {
                        return false;
                    }else{
                        return state;
                    }
                }
                if (*cur != '\0') return false;
                else return state;
            }else{
                if (*cur != '\0') {
                    return false;
                }else{
                    return state;
                }
            }

        }else{
            state = false;
            return state;
        }
        return state;
    }

};


// int main(int argc, char const *argv[]) {
//     char* p = "hello";
//     std::cout << p[0] << '\n'<<*(++p);
//     return 0;
// }
