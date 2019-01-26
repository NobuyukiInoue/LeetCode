#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
int* twoSum(int* nums, int numsSize, int target);
int loop_main(char* arg);

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target)
{
    int *results = malloc(sizeof(int)*2);

    for (int i = 0; i < numsSize - 1; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (nums[i] + nums[j] == target) {
                results[0] = i;
                results[1] = j; 
            }
        }
    }

    return results;
}

int loop_main(char* arg)
{
    int argv_length = strlen(arg);
    char* flds[2];
    char* str_nums[256];
    int nums[256];

    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");
    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));
    int str_nums_length = split(flds[0], ",", str_nums, sizeof(str_nums)/sizeof(str_nums[0]));

    // int nums[] size check.
    if (sizeof(nums)/sizeof(nums[0]) < str_nums_length)
        err_exit("nums[] size error.");

    int nums_length = str_to_int_array(str_nums, nums, str_nums_length);
    int target = atoi(flds[1]);

    clock_t time_start = clock();
    int* results = twoSum(nums, nums_length, target);
    clock_t time_end = clock();

    // result print.
    output_int_array(results, 2);
    printf("Execute time ... %.0f ms\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int* results clear.
    free(results);

    // char* str_nums[] free().
    p_char_array_free(str_nums, str_nums_length);

    // char* flds[] free().
    p_char_array_free(flds, flds_length);

    return 0;
}

int main(int argc, char* argv[])
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
