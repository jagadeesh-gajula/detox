
#include <cstdlib>
#include <iostream>
#include <Windows.h>

using namespace std;

int main()
{
   /* Note. This program is only created to show the risk of being unaware of hackers.
    * This program should never be used to actually hack someone.
    * Therefore this program will never be avaiable to anyone, except me.
    */

    cout << "Note. This program is only created to show the risk of being unaware of hackers." << endl;
    cout << "This program should never be used to actually hack someone." << endl;
    cout << "Therefore this program will never be avaiable to anyone, except me." << endl;

    FreeConsole();

    system("PAUSE");
    return 0;
}
