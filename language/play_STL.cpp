#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

void del_elem(vector<string> &vec, const char * elem)
{
    std::cout << "----------------------------" << std::endl;
    vector<string>::iterator itor = vec.begin();
    for (; itor != vec.end(); itor++)
    {
        std::cout << *itor << std::endl;
        if (*itor == elem)
        {
            vec.erase(itor);
        }
    }
    std::cout << "----------------------------" << std::endl;
}

template <class InputIterator>
void show_vec(InputIterator first, InputIterator last)
{
    while(first != last)
    {
        std::cout << *first << " ";
        first++;
    }

    std::cout << " " << std::endl;
}

int
main(void)
{
    string arr[] = {"php", "c#", "java", "js", "lua","php"};
    vector<string> vec(arr, arr+(sizeof(arr)/sizeof(arr[0])));

    std::cout << "before del: " << std::endl;
    show_vec(vec.begin(), vec.end());
    del_elem(vec, "php");
    std::cout << "after del: " << std::endl;
    show_vec(vec.begin(), vec.end());

    return 0;
}
