#include <iostream>
#include<stdlib.h>
#include <stdio.h>
#include<string>


using namespace std;

int main()
{

    string st ="command";
    st=system("tasklist");

    string str1 = "python.exe";


    size_t found = st.find(str1);
    if (found != string::npos)
        cout << "First occurrence is " << found << endl;

    int k;
    cin>>k;
    return 0;
}
