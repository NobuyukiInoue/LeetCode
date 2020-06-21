#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "include/mylib.h"

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
    ml_replace(arg, "\"", "");
    ml_replace(arg, "[", "");
    ml_replace(arg, "]", "");
    ml_replace(arg, "\n", "");

    int *nums;
    int nums_Length = ml_str_to_int_array(arg, &nums);
    ml_print_int_array("nums", nums, nums_Length);

    clock_t time_start = clock();

    int result = arrayPairSum(nums, nums_Length);

    clock_t time_end = clock();

    printf("result = %d\n", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int nums[] clear.
    free(nums);

    return 0;
}

int main(int argc, char *argv[])
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
