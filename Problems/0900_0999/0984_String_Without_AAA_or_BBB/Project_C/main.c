#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "lib/mylib.h"

/* Function prototype declaration */
char* strWithout3a3b(int A, int B);


int loop_main(char* arg);


#define RESULT_MAX_SIZE    201

char* strWithout3a3b(int A, int B)
{
    char* resultStr = (char *)malloc(sizeof(char)*RESULT_MAX_SIZE);
    resultStr[0] = '\0';

    if (A + B > RESULT_MAX_SIZE)
        ml_err_exit("strWithout3a3b() resultStr size over.\n");

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
        ml_err_exit("strWithout3a3b() resultStr size over.\n");

    return resultStr;    
}

int loop_main(char* arg)
{
    ml_replace(arg, "[", "");
    ml_replace(arg, "]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, ",", flds, sizeof(flds)/sizeof(flds[0]));

    int A = strtol(flds[0], NULL, 10);
    int B = strtol(flds[1], NULL, 10);
    printf("A = %d, B = %d\n", A, B);

    clock_t time_start = clock();

    char* results = strWithout3a3b(A, B);

    clock_t time_end = clock();

    // result print.
    printf("result = %s\n", results);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int* results clear.
    free(results);

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
