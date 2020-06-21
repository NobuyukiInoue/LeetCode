#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "include/mylib.h"

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
    ml_replace(arg, "\"", "");
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    char *s, *t;
    if (arg[0] != '\0') {
        s = (char *)malloc(sizeof(char)*strlen(flds[0]));
        t = (char *)malloc(sizeof(char)*strlen(flds[1]));
        strcpy(s, flds[0]);
        strcpy(t, flds[1]);
    } else {
        s = "";
        t = "";
    }

    printf("s = %s, t = %s\n", s, t);

    clock_t time_start = clock();

    char result = findTheDifference(s, t);

    clock_t time_end = clock();

    // result print.
    printf("result = %c\n", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char s[], t[] clear.
    free(t);
    free(s);

    // char* flds[] clear.
    ml_p_char_array_free(flds, flds_length);

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
