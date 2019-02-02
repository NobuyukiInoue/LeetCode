#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Function prototype declaration */
int searchInsert(int* nums, int numsSize, int target);
int loop_main(char* arg);

int searchInsert(int* nums, int numsSize, int target)
{
    int i;
    
    for ( i = 0; i < numsSize; i++ ) {
        if ( nums[i] < target ) {
            continue;
        }
        else if ( nums[i] >= target ) {
            return i;
        }
    }
    
    return i;
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
    int str_numsSize = split(flds[0], ",", str_nums, sizeof(str_nums)/sizeof(str_nums[0]));

    // int nums[] size check.
    if (sizeof(nums)/sizeof(nums[0]) < str_numsSize)
        err_exit("nums[] size error.");

    int numsSize = str_to_int_array(str_nums, nums, str_numsSize);
    int target = atoi(flds[1]);

    clock_t time_start = clock();
    int results = searchInsert(nums, numsSize, target);
    clock_t time_end = clock();

    // result print.
    printf("result = %d\n", results);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* str_nums[] free().
    p_char_array_free(str_nums, str_numsSize);

    // char* flds[] free().
    p_char_array_free(flds, flds_length);

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
