#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "../../../mylib_C/mylib.h"

//int** generate(int numRows, int** columnSizes);
int** generate(int numRows, int* returnSize, int** returnColumnSizes);

void print_data(int *data, int size);
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

void print_data(int *data, int size)
{
    if (size <= 0)
        return;
    
    printf("%d", data[0]);
    for (int i = 1; i < size; ++i) {
        printf(",%d", data[i]);
    }

    printf("\n");
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

    // int nums[] size check.
    int numRows = atoi(arg);
    printf("numRows = %d\n", numRows);

    clock_t time_start = clock();

    int *returnSize;
    int **returnColumnSizes;
    int **result;

//  returnSize = (int*)malloc(sizeof(int));
    returnColumnSizes = (int **)malloc(numRows*sizeof(int *));
    result = generate(numRows, returnSize, returnColumnSizes);

    clock_t time_end = clock();

    // result print.
    for (int i = 0; i < numRows; ++i) {
        printf("returnColumnSizes[%d] = %d, result[%d] = ", i, (*returnColumnSizes)[i], i);
        print_data(result[i], (*returnColumnSizes)[i]);
    }

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int** result clear.
    free(result);

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
