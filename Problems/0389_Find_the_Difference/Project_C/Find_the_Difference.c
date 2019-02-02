#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
char findTheDifference(char* s, char* t);
int loop_main(char* arg);

char findTheDifference(char* s, char* t)
{
    int sum = t[0];
    int t_Size = strlen(t);

    for(int i = 1; i < t_Size; i++)
        sum = sum + t[i] - s[i - 1];

    return (char)sum;
}

int loop_main(char* arg)
{
    int argv_length = strlen(arg);
    char* flds[2];

    replace(arg, "\"", "");
    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");
    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    char* s = flds[0];
    char* t = flds[1];

    printf("s = %s, t = %s\n", s, t);

    clock_t time_start = clock();
    char result = findTheDifference(s, t);
    clock_t time_end = clock();

    // result print.
    printf("result = %c\n", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* flds[] free().
    p_char_array_free(flds, flds_length);

    return 0;
}

int main(int argc, char* argv[])
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

    while((fgets(line, fgets_MAX - 1, fp)) != NULL) {
        trim(line);
        if (*line == '\0')
            continue;
        printf("arg = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
