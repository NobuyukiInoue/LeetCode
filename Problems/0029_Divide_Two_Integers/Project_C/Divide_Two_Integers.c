#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>

#include "mylib.h"

/* Function prototype declaration */
int divide(int dividend, int divisor);
int loop_main(char* arg);

typedef unsigned int uint;

int divide(int dividend, int divisor)
{
    if(divisor == 0 | (dividend  == INT_MIN && divisor == -1))
        return INT_MAX;
    
    bool sign = (dividend > 0)^(divisor>0);
    uint dd = (uint)(dividend < 0 ? -dividend : dividend);
    uint dr = (uint)(divisor < 0? -divisor : divisor);
    int reminder = 0;
    
    for (int i = 31; i >= 0; i--)
    {
        if ((dd >> i) >= dr)
        {
            reminder = reminder << 1 | 0x01;
            dd -= dr << i;
        } else
            reminder = reminder << 1;
    }
    return sign? -reminder : reminder;
}

int loop_main(char* arg)
{
    int argv_length = strlen(arg);
    char* flds[2];
    int dividend, divisor;

    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");
    split(arg, ",", flds);
    dividend = strtol(flds[0], NULL, 10);
    divisor = strtol(flds[1], NULL, 10);

    printf("result = %d\n", divide(dividend, divisor));

    return 0;
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char str[256];

    if (argc < 2) {
        printf("Usage %s <testdatafile>\n", argv[0]);
        return -1;
    }

    // File Open
    fp = fopen(argv[1], "r");

    if (fp == NULL) {
        printf("%s Open Failed...\n", argv[1]);
        return -1;
    }

    while((fgets(str, 256, fp)) != NULL) {
        printf("arg = %s\n", str);
        loop_main(str);
    }

    fclose(fp);
    return 0;
}