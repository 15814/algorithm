
class Solution {
public:
    string ReverseSentence(string str) {
        if (str.empty()) {
            return str;
        }
        str = reverse(str);
        string substr;
        string result;
        for (size_t i = 0; i < str.size(); i++) {
            if (str[i] != ' ') {
                substr += str[i];
            }else{
                result += reverse(substr)+' ';
                substr = "";
            }
        }
        result += reverse(substr);

        return result;
    }

    string reverse(string str){
        if (str.empty()) {
            return str;
        }
        size_t start = 0;
        size_t end = str.size()-1;
        while (start < end) {
            swap(str[start],str[end]);
            start++;
            end--;
        }
        return str;
    }
};
