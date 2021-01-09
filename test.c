#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

void ClearScreen()
{
    HANDLE hStdOut;
    CONSOLE_SCREEN_BUFFER_INFO csbi;
    DWORD count;
    DWORD cellCount;
    COORD homeCoords = {0, 0};

    hStdOut = GetStdHandle(STD_OUTPUT_HANDLE);
    if (hStdOut == INVALID_HANDLE_VALUE)
        return;

    /* Get the number of cells in the current buffer */
    if (!GetConsoleScreenBufferInfo(hStdOut, &csbi))
        return;
    cellCount = csbi.dwSize.X * csbi.dwSize.Y;

    /* Fill the entire buffer with spaces */
    if (!FillConsoleOutputCharacter(
            hStdOut,
            (TCHAR)' ',
            cellCount,
            homeCoords,
            &count))
        return;

    /* Fill the entire buffer with the current colors and attributes */
    if (!FillConsoleOutputAttribute(
            hStdOut,
            csbi.wAttributes,
            cellCount,
            homeCoords,
            &count))
        return;

    /* Move the cursor home */
    SetConsoleCursorPosition(hStdOut, homeCoords);
}

void status_sleepy()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (-)(-) :\n         ,'   --   `.\n         :          :\n         :          :\n   -slp- `._m____m_,' \n";
    char pet2[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (o)(o) :\n         ,'   --   `.\n         :          :\n         :          :\n   -slp- `._m____m_,' \n";
    char pet3[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (o)(o) :\n         ,'    O   `.\n        :            :\n        :            :\n   -slp- `._m____m_,' \n";
    ClearScreen();
    while (1)
    {

        printf("%s\n", pet2);
        Sleep(500);
        ClearScreen();
        printf("%s\n", pet3);
        Sleep(500);
        ClearScreen();
        printf("%s\n", pet);
        Sleep(10);
        ClearScreen();
    }
}
int main()
{
    status_sleepy();
}