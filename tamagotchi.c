#include <stdio.h>
#include <string.h>
#include <time.h>
#include <stdlib.h>
#include <conio.h>

char face[] = "⠄⠄⠄⢰⣧⣼⣯⠄⣸⣠⣶⣶⣦⣾⠄⠄⠄⠄⡀⠄⢀⣿⣿⠄⠄⠄⢸⡇⠄⠄\n"
              "⠄⠄⠄⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄⠸⢀⣿⠄\n"
              "⠄⠄⢀⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥⣿⣿⠄\n"
              "⠄⠄⢸⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣿⠄\n"
              "⠄⢀⢸⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄⠉⠋⣰\n"
              "⠄⣼⣖⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿⠇⢀⣤\n"
              "⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥⣴⣿⡗\n"
              "⢀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠄\n"
              "⢸⣿⣦⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄\n"
              "⠘⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵⣾⠃⠄\n"
              "⠄⠘⣿⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿⠃⠄⠄\n"
              "⠄⠄⠈⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁⠄⠄⠄\n"
              "⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄⠄⠄⠄\n"
              "⠄⠄⠄⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄⢀⣠⣴\n"
              "⣿⣿⣿⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⣠⣴⣿⣿⣿\n";

char face2[] = "⡿⠉⠄⠄⠄⠄⠈⠙⠿⠟⠛⠉⠉⠉⠄⠄⠄⠈⠉⠉⠉⠛⠛⠻⢿⣿⣿⣿⣿⣿\n"
               "⠁⠄⠄⠄⢀⡴⣋⣵⣮⠇⡀⠄⠄⠄⠄⠄⠄⢀⠄⠄⠄⡀⠄⠄⠄⠈⠛⠿⠋⠉\n"
               "⠄⠄⠄⢠⣯⣾⣿⡿⣳⡟⣰⣿⣠⣂⡀⢀⠄⢸⡄⠄⢀⣈⢆⣱⣤⡀⢄⠄⠄⠄\n"
               "⠄⠄⠄⣼⣿⣿⡟⣹⡿⣸⣿⢳⣿⣿⣿⣿⣴⣾⢻⣆⣿⣿⣯⢿⣿⣿⣷⣧⣀⣤\n"
               "⠄⠄⣼⡟⣿⠏⢀⣿⣇⣿⣏⣿⣿⣿⣿⣿⣿⣿⢸⡇⣿⣿⣿⣟⣿⣿⣿⣿⣏⠋\n"
               "⡆⣸⡟⣼⣯⠏⣾⣿⢸⣿⢸⣿⣿⣿⣿⣿⣿⡟⠸⠁⢹⡿⣿⣿⢻⣿⣿⣿⣿⠄\n"
               "⡇⡟⣸⢟⣫⡅⣶⢆⡶⡆⣿⣿⣿⣿⣿⢿⣛⠃⠰⠆⠈⠁⠈⠙⠈⠻⣿⢹⡏⠄\n"
               "⣧⣱⡷⣱⠿⠟⠛⠼⣇⠇⣿⣿⣿⣿⣿⣿⠃⣰⣿⣿⡆⠄⠄⠄⠄⠄⠉⠈⠄⠄\n"
               "⡏⡟⢑⠃⡠⠂⠄⠄⠈⣾⢻⣿⣿⡿⡹⡳⠋⠉⠁⠉⠙⠄⢀⠄⠄⠄⠄⠄⠂⠄\n"
               "⡇⠁⢈⢰⡇⠄⠄⡙⠂⣿⣿⣿⣿⣱⣿⡗⠄⠄⠄⢀⡀⠄⠈⢰⠄⠄⠄⠐⠄⠄\n"
               "⠄⠄⠘⣿⣧⠴⣄⣡⢄⣿⣿⣿⣷⣿⣿⡇⢀⠄⠤⠈⠁⣠⣠⣸⢠⠄⠄⠄⠄⠄\n"
               "⢀⠄⠄⣿⣿⣷⣬⣵⣿⣿⣿⣿⣿⣿⣿⣷⣟⢷⡶⢗⡰⣿⣿⠇⠘⠄⠄⠄⠄⠄\n"
               "⣿⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⡟⢀⠃⠄⢸⡄⠁⣸\n"
               "⣿⠄⠄⠘⢿⣿⣿⣿⣿⣿⣿⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢄⡆⠄⢀⣪⡆⠄⣿\n"
               "⡟⠄⠄⠄⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣟⣻⣩⣾⣃⣴⣿⣿⡇⠸⢾\n";

char face3[] = "⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
               "⣿⣿⣿⣿⣿⣿⣿⣿⡇⢀⢀⠍⠙⢿⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿\n"
               "⠹⣿⣿⣿⣿⣿⣿⣿⠁⠈⢀⡤⢲⣾⣗⠲⣿⣿⣿⣿⣿⣿⣟⠻\n"
               "⡀⢙⣿⣿⣿⣿⣿⣿⢀⠰⠁⢰⣾⣿⣿⡇⢀⣿⣿⣿⣿⣿⣿⡄\n"
               "⣇⢀⢀⠙⠷⣍⠛⠛⢀⢀⢀⢀⠙⠋⠉⢀⢀⢸⣿⣿⣿⣿⣿⣷\n"
               "⡙⠆⢀⣀⠤⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⣿⣿⣿⣿⣿\n"
               "⣷⣖⠋⠁⢀⢀⢀⢀⢀⢀⣀⣀⣄⢀⢀⢀⢀⢸⠏⣿⣿⣿⢿⣿\n"
               "⣿⣷⡀⢀⢀⢀⢀⢀⡒⠉⠉⢀⢀⢀⢀⢀⢀⢈⣴⣿⣿⡿⢀⡿\n"
               "⣿⣿⣷⣄⢀⢀⢀⢀⠐⠄⢀⢀⢀⠈⢀⣀⣴⣿⣿⣿⡿⠁⢀⣡\n"
               "⠻⣿⣿⣿⣿⣆⠢⣤⣄⢀⢀⣀⠠⢴⣾⣿⣿⡿⢋⠟⢡⣿⣿⣿\n"
               "⢀⠘⠿⣿⣿⣿⣦⣹⣿⣀⣀⣀⣀⠘⠛⠋⠁⡀⣄⣴⣿⣿⣿⣿\n";

char life1[] = "      $$$   $$$";
char life2[] = "     $$$$$ $$$$$";
char life3[] = "     $$$$$$$$$$$";
char life4[] = "       $$$$$$$";
char life5[] = "         $$$";
char life6[] = "          $";
char dead1[] = "      000   000";
char dead2[] = "     00000 00000";
char dead3[] = "     00000000000";
char dead4[] = "       0000000";
char dead5[] = "         000";
char dead6[] = "          0";

int heart = 5;
int food_bar = 5;
int energy_bar = 5;
int happiness = 5;
int balance = 50;
int count = 0;
int wife = 0;

char food1[] = "     ,--./,-.";
char food2[] = "    / #      \\";
char food3[] = "   |          |";
char food4[] = "    \\        / ";
char food5[] = "     `._,._,'";

char food1_empty[] = "    ,--./,-.";
char food2_empty[] = "   /,-._.--~\\";
char food3_empty[] = "    __}  {";
char food4_empty[] = "   \\`-._,-`-,";
char food5_empty[] = "    `._,._,' ";

char energy1[] = "         ____";
char energy2[] = "    ____|    \\";
char energy3[] = "   (____|     `._____";
char energy4[] = "    ____|       _|___";
char energy5[] = "   (____|     .'";
char energy6[] = "        |____/";

void the_pet();
void life();

void energy()
{
    printf("ENERGY:\n");
    int i;
    for (i = 0; i < energy_bar; i++)
    {
        printf("%s        ", energy1);
    }
    printf("\n");
    for (i = 0; i < energy_bar; i++)
    {
        printf("%s       ", energy2);
    }
    printf("\n");
    for (i = 0; i < energy_bar; i++)
    {
        printf("%s", energy3);
    }
    printf("\n");
    for (i = 0; i < energy_bar; i++)
    {
        printf("%s", energy4);
    }
    printf("\n");
    for (i = 0; i < energy_bar; i++)
    {
        printf("%s     ", energy5);
    }
    printf("\n");
    for (i = 0; i < energy_bar; i++)
    {
        printf("%s       ", energy6);
    }
    printf("\n\n");
}
void food()
{
    printf("FOOD:\n");
    int i;
    if (food_bar == 0)
    {
        heart = heart - 1;
        happiness = happiness - 3;
        for (i = 0; i < 5; i++)
        {
            printf("%s  ", food1_empty);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s ", food2_empty);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s    ", food3_empty);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s ", food4_empty);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s ", food5_empty);
        }
        printf("\n");
    }
    else
    {
        for (i = 0; i < food_bar; i++)
        {
            printf("%s  ", food1);
        }
        printf("\n");
        for (i = 0; i < food_bar; i++)
        {
            printf("%s ", food2);
        }
        printf("\n");
        for (i = 0; i < food_bar; i++)
        {
            printf("%s", food3);
        }
        printf("\n");
        for (i = 0; i < food_bar; i++)
        {
            printf("%s", food4);
        }
        printf("\n");
        for (i = 0; i < food_bar; i++)
        {
            printf("%s  ", food5);
        }
        printf("\n");
    }
}
void status_alive()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (.)(.) :\n         ,'        `.\n         :          :\n         :          :\n   -ctr- `._m____m_,' \n";
    printf("YOUR PET:\n");
    printf("%s\n", pet);
    the_pet();
}
void status_hurt()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (;)(;) :\n         ,'  _--_  `.\n         :          :\n         :          :\n   -ctr- `._m____m_,' \n";
    printf("YOUR PET:\n");
    printf("%s\n", pet);
    the_pet();
}
void status_happy()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (^)(^) :\n         ,'  -__-  `.\n         :          :\n         :          :\n   -ctr- `._m____m_,' \n";
    printf("YOUR PET:\n");
    printf("%s\n", pet);
    the_pet();
}
void status_dead()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (X)(X) :\n         ,'   --   `.\n         :    U     :\n         :          :\n   -ded- `._m____m_,' \n";
    printf("YOUR PET DIED!\n");
    printf("%s\n", pet);
    the_pet();
}
void status_suicide()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (X)(X) :\n         ,'   --   `.\n         :    U     :\n         :          :\n   -ded- `._m____m_,' \n";
    printf("YOUR PET KILLED ITSELF!\n");
    printf("%s\n", pet);
    the_pet();
}

void status_sleepy()
{
    char pet[] = "            ,.  ,.\n            ||  ||\n           ,''--''.\n          : (-)(-)z:\n         ,'   --z  `.\n         :    Z     :\n         :          :\n   -slp- `._m____m_,' \n";
    printf("YOUR PET IS SLEEPING!\n");
    printf("%s\n", pet);
    the_pet();
}
void the_pet()
{
    life();
    printf("\n");
    food();
    printf("\n");
    energy();
    if (wife == 1)
    {
        printf("%s\n", face);
    }
    if (wife == 2)
    {
        printf("%s\n", face2);
    }
    if (wife == 3)
    {
        printf("%s\n", face3);
    }
}
void life()
{
    int i;
    printf("LIFE:\n");
    if (heart == 0)
    {
        for (i = 0; i < 5; i++)
        {
            printf("%s ", dead1);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s", dead2);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s", dead3);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s  ", dead4);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s    ", dead5);
        }
        printf("\n");
        for (i = 0; i < 5; i++)
        {
            printf("%s     ", dead6);
        }
        printf("\n\n");
        printf("=================================\n");
        printf("          AGE:%d\n", count);
        printf("=================================\n\n");
    }
    else
    {
        for (i = 0; i < heart; i++)
        {
            printf("%s ", life1);
        }
        printf("\n");
        for (i = 0; i < heart; i++)
        {
            printf("%s", life2);
        }
        printf("\n");
        for (i = 0; i < heart; i++)
        {
            printf("%s", life3);
        }
        printf("\n");
        for (i = 0; i < heart; i++)
        {
            printf("%s  ", life4);
        }
        printf("\n");
        for (i = 0; i < heart; i++)
        {
            printf("%s    ", life5);
        }
        printf("\n");
        for (i = 0; i < heart; i++)
        {
            printf("%s     ", life6);
        }
        printf("\n");
        printf("=================================\n");
        printf("          AGE:%d\n", count);
        printf("=================================\n\n");
    }
}
int main()
{
    int choice;
    char decision = 'y';
    status_alive();
    int dice, give_coin;
    int food_counter = 0;
    while (decision != 'n')
    {
        if (food_bar == 5)
        {
            food_counter++;
            if (food_counter % 2 == 0)
            {
                heart = heart + 1;
            }
        }
        else
        {
            food_counter = 0;
        }

        if (happiness <= 0 || heart == 0)
        {
            if (happiness <= 0)
            {
                status_suicide();
                return 0;
            }
            if (heart == 0)
            {
                status_dead();
                return 0;
            }
        }
        else
        {
            printf("\n");
            printf("YOUR PET IS FEELING: ");
            if (happiness > 0 && happiness <= 2)
            {
                printf("SUICIDAL\n");
            }
            if (happiness > 2 && happiness <= 4)
            {
                printf("SAD\n");
            }
            if (happiness > 4 && happiness <= 6)
            {
                printf("SATISFIED\n");
            }
            if (happiness > 6 && happiness <= 8)
            {
                printf("HAPPY\n");
            }
            if (happiness > 8 && happiness <= 10)
            {
                printf("HIGH\n");
            }
            printf("BALANCE: %dcoins\n", balance);
            printf("HAPPINESS: %d\n", happiness);
            printf("\n");
            printf("=================================\n");
            printf(" CHOOSE WHAT TO DO TO YOUR PET:\n");
            printf("=================================\n\n");
            printf("(1)HIT  (2)PET  (3)FEED(costs 10)  (4)SLEEP  (5)GET WIFE(1)  (6)GET WIFE(2)  (7)GET WIFE(3)\n\n");
            scanf("%d", &choice);
            if (choice == 1)
            {
                heart = heart - 1;
                happiness = happiness - 2;
                printf("\n");
                printf("=================================\n");
                printf("        YOU HIT YOUR PET!\n");
                printf("=================================\n\n");
                if (heart == 0)
                {
                    status_dead();
                    return 0;
                }
                else
                {
                    status_hurt();
                }
            }
            if (choice == 2)
            {
                happiness = happiness + 1;
                if (heart < 5)
                    heart = heart + 1;
                printf("=================================\n");
                printf("    YOU PLAYED WITH YOUR PET!\n");
                printf("=================================\n\n");
                status_happy();
            }
            if (choice == 3)
            {

                if (food_bar < 5)
                {
                    happiness = happiness + 0.5;
                    balance = balance - 10;
                    food_bar = food_bar + 1;
                    printf("=================================\n");
                    printf("      YOU FED YOUR PET!\n");
                    printf("=================================\n\n");
                    status_happy();
                }
                else
                {
                    printf("YOUR PET IS FULL!\n");
                }
            }
            if (choice == 4)
            {
                if (energy_bar == 5)
                {
                    printf("YOUR PET IS NOT FEELING TIRED!\n");
                }
                else
                {
                    energy_bar = 5;
                    printf("=================================\n");
                    printf("        YOU PET SLEPT!\n");
                    printf("=================================\n\n");
                    status_sleepy();
                }
            }
            if (choice == 5)
            {
                happiness = 10;
                energy_bar = 5;
                wife = 1;
                status_happy();
            }
            if (choice == 6)
            {
                happiness = 10;
                energy_bar = 5;
                wife = 2;
                status_happy();
            }
            if (choice == 7)
            {
                happiness = 10;
                energy_bar = 5;
                wife = 3;
                status_happy();
            }

            printf("Do you want to continue playing?(y/n): ");
            scanf("\n%c", &decision);
            dice = rand() % 4;
            if (dice == 2)
            {
                give_coin = 50 - (10 * (rand() % 4));
                printf("YOUR TAMAGOTCHI GAVE YOU %d COINS!!\n", give_coin);
                balance = balance + give_coin;
            }
            count++;
            if (count % 3 == 0)
            {
                food_bar = food_bar - 1;
            }
            if (count % 2 == 0)
            {
                energy_bar = energy_bar - 1;
            }
        }
    }
}
