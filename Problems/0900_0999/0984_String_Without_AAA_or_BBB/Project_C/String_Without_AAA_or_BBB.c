#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
char* strWithout3a3b(int A, int B);
int loop_main(char* arg);

#define RESULT_MAX_SIZE    201

char* strWithout3a3b(int A, int B)
{
    char* resultStr = (char *)malloc(sizeof(char)*RESULT_MAX_SIZE);
    resultStr[0] = '\0';

    if (A + B > RESULT_MAX_SIZE)
        err_exit("strWithout3a3b() resultStr size over.\n");

    while (A > B && B > 0) {
        strcat(resultStr, "aab");
        A -= 2;
        B--;
    }

    while (B > A && A > 0) {
        strcat(resultStr, "bba");
        B -= 2;
        A--;
    }

    if (A == 0 || B == 0) {
        if (B == 0) {        
            for (int i = 0; i < A; ++i)
                strcat(resultStr, "a");
        } else {
            for (int i = 0; i < B; ++i)
                strcat(resultStr, "b");
        }
    } else if (strlen(resultStr) == 0 || resultStr[strlen(resultStr) - 1] == 'a') {
        for (int i = 0; i < A; ++i)
            strcat(resultStr, "ba");
    } else {
        for (int i = 0; i < B; ++i)
            strcat(resultStr, "ab");
    }

    if (strlen(resultStr) > RESULT_MAX_SIZE)
        err_exit("strWithout3a3b() resultStr size over.\n");

    return resultStr;    
}

int loop_main(char* arg)
{
    int argv_length = strlen(arg);
    char* flds[2];
    char* str_nums[256];
    int nums[256];

    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");
    int flds_length = split(arg, ",", flds, sizeof(flds)/sizeof(flds[0]));
    int A = atoi(flds[0]);
    int B = atoi(flds[1]);

    clock_t time_start = clock();
    char* results = strWithout3a3b(A, B);
    clock_t time_end = clock();

    // result print.
    printf("result = %s\n", results);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int* results clear.
    free(results);

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
