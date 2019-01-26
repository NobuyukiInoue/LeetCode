#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
int arrayPairSum(int* nums, int numsSize);
static int compareInt(const void* a, const void* b);
int loop_main(char* arg);

int arrayPairSum(int* nums, int numsSize)
{
        qsort(nums, numsSize, sizeof(int), compareInt);
        int sum = 0;
        for (int i = 0; i < numsSize; i += 2)
            sum += nums[i];
        
        return sum;   
}

static int compareInt(const void* a, const void* b)
{
    int aNum = *(int*)a;
    int bNum = *(int*)b;

    return aNum - bNum;
}

int loop_main(char* arg)
{
    char* str_nums[256];
    int nums[256];

    replace(arg, "\"", "");
    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");

    int str_nums_Length = split(arg, ",", str_nums, sizeof(str_nums)/sizeof(str_nums[0]));
    str_to_int_array(str_nums, nums, str_nums_Length);

    clock_t time_start = clock();

    int result = arrayPairSum(nums, str_nums_Length);

    clock_t time_end = clock();

    printf("result = %d\n", result);
    printf("Execute time ... %.0f ms\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* str_nums[] free().
    p_char_array_free(str_nums, str_nums_Length);

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
