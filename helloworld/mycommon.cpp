/*
 *
 */

#include "mycommon.h"

using namespace std;
// cp string
char* CMyCommon::strcpy(char* dst, const char* src)
{
    if(dst == nullptr || src == nullptr)
    {
        return nullptr;
    }

    cout << "mark... \n";

    char* pos_mark = dst;
    while(*src != '\0')
    {
        cout << *src;
        *(dst++) = *(src++);
    }

    return pos_mark;
}

// merge 