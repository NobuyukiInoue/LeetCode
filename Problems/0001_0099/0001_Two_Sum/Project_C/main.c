#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "lib/mylib.h"

/* Function prototype declaration */
int* twoSum(int* nums, int numsSize, int target, int* returnSize);


int loop_main(char* arg);

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    // 132ms
    *returnSize = 2;
    int *results = malloc(sizeof(int)*(*returnSize));

    for (int i = 0; i < numsSize - 1; ++i) {
        for (int j = i + 1; j < numsSize; ++j) {
            if (nums[i] + nums[j] == target) {
                results[0] = i;
                results[1] = j;
                return results;
            }
        }
    }
    return results;
}

int loop_main(char* arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int *nums;      // nums[] ... malloc() by ml_str_to_array()
    int nums_length = ml_str_to_int_array(flds[0], &nums);
    ml_print_int_array("nums", nums, nums_length);

    int target = strtol(flds[1], NULL, 10);
    printf("target = %d\n", target);

    clock_t time_start = clock();

    int returnSize;
    int* results = twoSum(nums, nums_length, target, &returnSize);

    clock_t time_end = clock();

    // result print.
    ml_print_int_array("results", results, returnSize);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // int results[] clear.
    free(results);

    // int nums[] clear.
    free(nums);

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
