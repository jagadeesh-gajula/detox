#include<iostream>
#include<fstream>
#include<string>
#include<stdlib.h>
#include<stdio.h>

using namespace std;

int main() {
   string str;

   char data[100];

   ifstream ifile;
   ifile.open("status.txt");

   while (!ifile.eof()) {
      ifile.getline(data, 100);
      str=data;
   }

   ifile.close();
   if (str.size() < 3)
   {
       cout<<"python is not running";
       system("python");
   }
   else{
    cout<<"python is running";
   }
   return 0;
}
