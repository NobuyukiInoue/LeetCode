#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int* calc_next(int* data, int data_length);
void print_data(int *data, int size);
void test_Main(int num);
void test_Main2(int num);

/**
 * Return an array of arrays.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */

int** generate(int numRows, int** columnSizes)
{
    int** returnArray = (int**)malloc(sizeof(int*)*numRows);
    *columnSizes = (int*)malloc(sizeof(int)*numRows);
    for(int i=0;i<numRows;i++){
        (*columnSizes)[i] = i+1;
        returnArray[i] = (int*)malloc(sizeof(int)*(i+1));
        returnArray[i][0] = 1;
        returnArray[i][i] = 1;
        for(int j=1;j<i;j++){
            returnArray[i][j] = returnArray[i-1][j] + returnArray[i-1][j-1];
        }
    }
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

void test_Main(int num)
{
    int **data;
    int i;

    data = (int **)malloc(num*sizeof(int **));

    for (i = 0; i < num; ++i) {
        data[i] = (int *)malloc( (i + 1) * sizeof(int) );
    }

    data[0][0] = 1;

    for (i = 0; i < num; ++i)
        data[i + 1] = calc_next(data[i], i + 1);

    for (i = 0; i < num; ++i) {
        printf("data[%d] = ", i);
        print_data(data[i], i + 1);
    }
}

void test_Main2(int num)
{
    int **columnsSizes;
    int **result;

    result = generate(num, columnsSizes);

    for (int i = 0; i < num; ++i) {
        printf("columnsSizes[%d] = %d, result[%d] = ", i, *columnsSizes[i], i);
        print_data(result[i], *columnsSizes[i]);
    }

}

void main(int argc, char *args[])
{
    printf("============= test_Main() ==============\n");
    test_Main(10);

    printf("============= test_Main2() ==============\n");
    test_Main2(10);
}

