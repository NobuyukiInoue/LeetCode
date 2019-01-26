#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
bool checkRecord(char* s);

void sort(int nums[], int length);
int loop_main(char* arg);

bool checkRecord(char* s)
{
    int count_A = 0, count_L = 0;

    while(*s != '\0') {
        if (*s == 'A')
            if (++count_A > 1)
                return false;
        if (*s == 'L')
            if (*(s + 1) == 'L' && *(s + 2) == 'L')
                return false;
        s++;
    }

    return true;
}

int loop_main(char* arg)
{
    replace(arg, "\"", "");
    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");
    char* s = arg;

    clock_t time_start = clock();

    bool result = checkRecord(s);

    clock_t time_end = clock();

    if (result)
        printf("result = true\n");
    else
        printf("result = false\n");

    printf("Execute time ... %.0f ms\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

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
