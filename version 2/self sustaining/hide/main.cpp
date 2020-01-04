// ForWinXp

#define _WIN32_WINNT 0x0501

#include <windows.h>

#include <stdio.h>

#include <psapi.h>



void PrintProcessNameAndID(DWORD processID)

{

   // Initialize or default to "unknown"

   char szProcessName[MAX_PATH] = "<unknown>";

   // Get a handle to the process.

    HANDLE hProcess = OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, FALSE, processID);

   // Get the process name.

   if (hProcess != NULL)

    {

        HMODULE hMod;

        DWORD cbNeeded;

       if (EnumProcessModules(hProcess, &hMod, sizeof(hMod), &cbNeeded))

        {

            GetModuleBaseName(hProcess, hMod, szProcessName, sizeof(szProcessName));

        }

    }

   // Print the process name and identifier.

    printf("%-30s   %5u\n", szProcessName, processID);

    CloseHandle(hProcess);

}



int main()

{

   // Get the list of process identifiers.

    DWORD aProcesses[1024], cbNeeded, cProcesses;

   unsignedint i;

   // If fail...

   if (!EnumProcesses(aProcesses,sizeof(aProcesses), &cbNeeded))

       return 1;// or print some meaningful message...

   else

        printf("Enumprocesses() is OK.\n");

   // Calculate how many process identifiers were returned.

    cProcesses = cbNeeded / sizeof(DWORD);

   // Print the name and process identifier for each process.

    printf("Process Name                 Process ID\n");

    printf("============                 ==========\n");

   for (i = 0; i < cProcesses; i++)

        PrintProcessNameAndID(aProcesses[i]);

      return 0;

}
