#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#include "mylib.h"

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
    split(arg, "],[", flds);

    int nums_length = split(flds[0], ",", str_nums);
    str_to_int_array(str_nums, nums, nums_length);

    int target = atoi(flds[1]);

    int *result = twoSum(nums, nums_length, target);
    output_p_int_array(result, 2);

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
