#include <stdio.h>

void main(void)
{
    char *str[] = {"Hello ", "C ", "World!"};
    int str_length;

    str_length = sizeof(str) / sizeof(char *);
    printf("str_length = %d\n", str_length);

    for (int i = 0; i < str_length; ++i)
        printf("%s", str[i]);

}