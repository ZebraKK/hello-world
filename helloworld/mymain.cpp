
#include <iostream>
#include <utility>
#include <string>
#include <vector>

using namespace std;

#include "mycommon.h"

/*
void foo(const std::string& n)
{
    std::cout << "lvalue" << std::endl;
}

void foo(std::string&& n)
{                              
    std::cout << "rvalue" << std::endl;
}

void bar()
{
    foo("hello");                // rvalue
    std::string a = "world";      
    foo(a);                      // lvalue
    foo(std::move(a));           // rvalue
}
*/

void bar(const int& x)
{
  std::cout << "lvalue" << std::endl;
}

void bar(int&& x)
{
  std::cout << "rvalue" << std::endl;
}

template <typename T>
void foo(T&& x)
{
  bar(x);
  bar(std::forward<T>(x));
}

void overloaded(const int& x)
{
  std::cout << "[lvalue]" << std::endl;
}

void overloaded(int&& x)
{
  std::cout << "[rvalue]" << std::endl;
}

template <class T> void fn(T&& x)
{
  overloaded(x);
  overloaded(std::forward<T>(x));
}

int main()
{
    cout << "hello world" << endl;
    //char ch[64];
/*
    std::vector<std::string> a = {"hello", "world"};
    std::vector<std::string> b;

    b.push_back("hello");
    b.push_back(std::move(a[1]));

    std::cout << "bsize: " << b.size() << std::endl;
    for (std::string& x: b)
    {
        std::cout << x << std::endl;
    }

    bar();
*/

  int x = 10; 
  foo(x);
  foo(10);

  int i = 10; 
  overloaded(std::forward<int>(i));
  overloaded(std::forward<int&>(i));
  overloaded(std::forward<int&&>(i));
  
  fn(i);
  fn(std::move(i));

/*
    char ping[] = "hello 123";
    char pang[64] = {};
    cout <<"ping ->" << ping <<endl;
    cout <<"pang ->" << pang <<endl;
    cout << "-----------\n" ;

    CMyCommon mycommon;
    char* p_data = mycommon.strcpy(pang, ping);
    cout <<"p-->" << p_data << "\n" << endl;
*/



/*
    std::string str;
    while(1)
    {
        cout << "please enter ...\n";
        str.clear();
        cin >> str;

        cout << "we got --> " << str << " <--" << endl;
        if(str == "quit")
        {
            cout << "got \'q\' and exit \n";
            break;
        }
    }
*/

    cout << "Hello, OK ^_^" << endl;
    return 0;
}

