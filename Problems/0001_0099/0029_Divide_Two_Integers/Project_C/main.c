#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>
#include <time.h>

#include "lib/mylib.h"

/* Function prototype declaration */
int divide(int dividend, int divisor);


int loop_main(char* arg);


typedef unsigned int uint;

int divide(int dividend, int divisor)
{
    if(divisor == 0 || (dividend  == INT_MIN && divisor == -1))
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
    ml_replace(arg, "[", "");
    ml_replace(arg, "]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, ",", flds, sizeof(flds)/sizeof(flds[0]));

    int dividend, divisor;
    dividend = strtol(flds[0], NULL, 10);
    divisor = strtol(flds[1], NULL, 10);
    printf("dividend = %d, divisor = %d\n", dividend, divisor);

    clock_t time_start = clock();

    int result = divide(dividend, divisor);

    clock_t time_end = clock();

    printf("result = %d\n\n", result);

    // char* flds[] clear.
    ml_p_char_array_free(flds, flds_length);

    return 0;
}

int main(int argc, char *argv[])
{
#define fgets_MAX   65536
    FILE *fp;
    char line[fgets_MAX];

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

    while ((fgets(line, fgets_MAX - 1, fp)) != NULL) {
        ml_trim(line);
        if (*line == '\0')
            continue;
        printf("arg = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
