#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "../../../mylib_C/mylib.h"

int** generate(int numRows, int** columnSizes);
int* calc_next(int* data, int data_length);
void print_data(int *data, int size);
int loop_main(char* arg);

/**
 * Return an array of arrays.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int** generate(int numRows, int** columnSizes)
{
    int** returnArray = (int**)malloc(sizeof(int*)*numRows);
    *columnSizes = (int*)malloc(sizeof(int)*numRows);
    for (int i = 0; i < numRows; i++) {
        (*columnSizes)[i] = i + 1;
        returnArray[i] = (int*)malloc(sizeof(int)*(i+1));
        returnArray[i][0] = 1;
        returnArray[i][i] = 1;
        for (int j = 1; j < i; j++) {
            returnArray[i][j] = returnArray[i - 1][j] + returnArray[i - 1][j - 1];
        }
    }
    return returnArray;
}

/*
int** generate(int numRows, int** columnSizes)
{
    int **data;
    int i;

    data = (int **)malloc(numRows*sizeof(int *));
    *columnSizes = (int *)malloc(numRows*sizeof(int));

    for (i = 0; i < numRows; ++i) {
        data[i] = (int *)malloc( (i + 1) * sizeof(int) );
    }

    data[0][0] = 1;
    *columnSizes[0] = 1;

    for (i = 0; i < numRows; ++i) {
        data[i + 1] = calc_next(data[i], i + 1);
        *columnSizes[i + 1] = *columnSizes[i] + 1;
    }

    return data;
}

int* calc_next(int* data, int data_length)
{
    int *result;
    int result_length;
    
    // mallocで生成した配列の場合は、要素数の取得に失敗する
//  data_length = sizeof(data) / sizeof(int);

    result_length = data_length + 1;
    result = (int *)malloc(result_length*sizeof(int));

//  printf("sizeof(data) = %d, data_length = %d, result_length = %d, result_size = %d\n", sizeof(data), data_length, result_length, result_length*sizeof(int));

    result[0] = 1;
    result[result_length - 1] = 1;

    int i;
    for(i = 1; i < result_length / 2; ++i) {
        if (i - 1 >= 0) {
            result[i] = data[i - 1] + data[i];
            result[result_length - 1 - i] = data[data_length - 1 - i + 1] + data[data_length - 1 - i];
        }
    }

    if (result_length % 2 == 1)
        result[i] =  data[i - 1] + data[i];

    return result;
}
*/

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

    int **columnsSizes;
    int **result;
    result = generate(numRows, columnsSizes);

    clock_t time_end = clock();

    // result print.
    for (int i = 0; i < numRows; ++i) {
        printf("columnsSizes[%d] = %d, result[%d] = ", i, *columnsSizes[i], i);
        print_data(result[i], *columnsSizes[i]);
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
