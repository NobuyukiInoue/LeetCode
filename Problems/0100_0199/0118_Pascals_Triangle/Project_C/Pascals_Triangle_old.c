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
    int **data;
    int i;

    data = (int **)malloc(numRows*sizeof(int *));
    *columnSizes = (int *)malloc(numRows*sizeof(int ));

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

