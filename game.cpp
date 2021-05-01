#include <stdio.h>
#include <conio.h>
#include <time.h>
#include <stdlib.h>

#define GROUND_BASE 19
#define TAMAGOTCHI_HEIGHT 8
#define GROUND_DEPTH 4
#define AIR_TIME 5;

int pos_x = (GROUND_BASE - GROUND_DEPTH + 1) - TAMAGOTCHI_HEIGHT, pos_y = 0;
int jump;
int jump_timer = 0;
int jump_condition = 0;
int counter_start = 0;
float myclock = clock() / 1000000.0;

void Background(char bg_array[20][211])
{
    //sleep(1);
    int i, j;
    system("clear");
    for (i = 0; i < 20; i++)
    {
        for (j = 0; j < 211; j++)
        {
            textbackground(GREEN);

            printf("%c", bg_array[i][j]);
        }
        printf("\n");
    }
    //printf("Game Time = %d\n", counter_start / CLOCKS_PER_SEC);
}

void copy(char pet[], char bg_array[20][211], int *pos_y, int *pos_x)
{
    int i, j, k = 0;
    j = 0;
    for (i = 0; i < 20; i++)
    {
        for (j = 0; j < 211; j++)
        {
            bg_array[i][j] = ' ';
            if (i >= 16)
            {
                bg_array[i][j] = '=';
            }
            if (i >= 17)
            {
                if (i >= 17)
                {
                    bg_array[i][j] = '#';
                }
                bg_array[i][j] = ';';
            }
            if (i >= 18)
            {
                bg_array[i][j] = '#';
            }
        }
    }
    i = 0;
    for (j = 0; k < 169; j++)
    {
        if (pet[k] == '\n')
        {
            i++;

            j = 0;
            k++;
        }
        //if (bg_array[i + *pos_x][j + *pos_y] == ' ' )

        bg_array[i + *pos_x][j + *pos_y] = pet[k];
        k++;

        /*else
        {
            if (bg_array[i + *pos_x][j + *pos_y] == '=')
            {
                *pos_x -= 1;
                printf("height = %d\n", *pos_x);
                return;
            }
        }*/
    }
}

void pos(char bg_array[20][211], char array_paddle[8], int x, int y)
{
    int i, j;
    int k = 0;
    for (i = 0; i < 20; i++)
    {
        for (j = 0; j < 211; j++)
        {
            bg_array[i][j] = ' ';
        }
    }
    for (i = x, j = y; j < (y + 8); j++)
    {
        bg_array[i][j] = array_paddle[k];
        printf("%d\n", k);
        k++;
    }
    if (i >= 17)
    {
        bg_array[i][j] = '#';
    }
}

int main()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (.)(.) :\n         ,'        `.\n         :          :\n         :          :\n   -ctr- `._m____m_,' \n";
    int i, j;
    char key;
    char bg_array[20][211];
    /* for (i = 0; i < 20; i++)
    {
        for (j = 0; j < 211; j++)
        {
            bg_array[i][j] = ' ';
            if (i >= 16)
            {
                bg_array[i][j] = '=';
            }
            if (i >= 17)
            {
                bg_array[i][j] = '#';
            }
        }
    }*/

    //Background(bg_array);
    char array_paddle[8] = {'#', '=', '=', '=', '=', '=', '=', '#'};
    /*  pos(bg_array, array_paddle, pos_x, pos_y);
    Background(bg_array);*/
    /*while (1)
    {
        
        if (kbhit())
        {
            key = getchar();
            if (key == 'd')
            {
                clrscr();
                pos_y += 1;
                pos(bg_array, array_paddle, pos_x, pos_y);
                Background(bg_array);
            }
            if (key == 'a')
            {
                clrscr();
                pos_y -= 1;
                pos(bg_array, array_paddle, pos_x, pos_y);
                Background(bg_array);
            }
        }
    }*/
    //clrscr();
    //pos_x = 0;
    copy(pet, bg_array, &pos_y, &pos_x);
    Background(bg_array);

    while (1)
    {
        myclock = clock() / CLOCKS_PER_SEC;
        counter_start = clock();
        if (((counter_start / CLOCKS_PER_SEC) - jump_timer) >= 1 && jump_condition == 1)
        {
            pos_x = (GROUND_BASE - GROUND_DEPTH + 1) - TAMAGOTCHI_HEIGHT;
            copy(pet, bg_array, &pos_y, &pos_x);
            Background(bg_array);
            jump_condition = 0;
        }

        if (kbhit())
        {
            key = getchar();
            if (key == 'p')
            {
                clrscr();
            }
            if (key == 'd')
            {
                //clrscr();
                pos_y += 1;
                //printf("%d\n",pos_y);
                copy(pet, bg_array, &pos_y, &pos_x);

                Background(bg_array);
            }
            if (key == 'a')
            {
                //clrscr();
                pos_y -= 1;
                //printf("%d\n",pos_y);
                copy(pet, bg_array, &pos_y, &pos_x);
                Background(bg_array);
            }
            if (key == 'w')
            {

                //clrscr();
                pos_x -= 2;
                jump_timer = clock()/1000000;
                jump_condition = 1;

                copy(pet, bg_array, &pos_y, &pos_x);
                Background(bg_array);
            }

            /*if (key == 's')
            {
                //clrscr();
                pos_x += 1;

                copy(pet, bg_array, &pos_y, &pos_x);
                Background(bg_array);
                
            }*/
        }
        if (((clock() / 1000000.0) - myclock >= 0) && ((clock() / 1000000.0) - myclock <= 0.000008))
        {

            //printf("%d\n", (clock() / CLOCKS_PER_SEC));
            copy(pet, bg_array, &pos_y, &pos_x);
            Background(bg_array);
        }
        //printf("difference = %f\n",(clock()/1000000.00000) - (counter_start/1000000.0000) );
    }
}