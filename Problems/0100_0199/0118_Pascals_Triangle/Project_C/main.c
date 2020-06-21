#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "include/mylib.h"

//int** generate(int numRows, int** columnSizes);
int** generate(int numRows, int* returnSize, int** returnColumnSizes);

int loop_main(char* arg);

/**
 * Return an array of arrays.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */


//int** generate(int numRows, int** columnSizes)
int** generate(int numRows, int* returnSize, int** returnColumnSizes)
{
    int** returnArray = (int**)malloc(sizeof(int*)*numRows);
    *returnColumnSizes = (int*)malloc(sizeof(int)*numRows);
    for (int i = 0; i < numRows; i++) {
        (*returnColumnSizes)[i] = i + 1;
        returnArray[i] = (int*)malloc(sizeof(int)*(i+1));
        returnArray[i][0] = 1;
        returnArray[i][i] = 1;
        for (int j = 1; j < i; j++) {
            returnArray[i][j] = returnArray[i - 1][j] + returnArray[i - 1][j - 1];
        }
    }
    *returnSize = numRows;
    return returnArray;
}

int loop_main(char* arg)
{
    ml_replace(arg, "[", "");
    ml_replace(arg, "]", "");
    ml_replace(arg, "\n", "");

    int numRows = strtol(arg, NULL, 10);
    printf("numRows = %d\n", numRows);

    clock_t time_start = clock();

    int *returnSize;
    int **returnColumnSizes;
    int **result;

    returnColumnSizes = (int **)malloc(numRows*sizeof(int *));
    result = generate(numRows, returnSize, returnColumnSizes);

    clock_t time_end = clock();

    // result print.
    for (int i = 0; i < numRows; ++i) {
        printf("returnColumnSizes[%d] = %d, result[%d]", i, (*returnColumnSizes)[i], i);
        ml_print_int_array("", result[i], (*returnColumnSizes)[i]);
    }

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int* result[] clear.
    free(result);

    // int returnColumnSize[] clear.
    free(returnColumnSizes);

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
        ml_trim(line);
        if (*line == '\0')
            continue;
        printf("arg = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
