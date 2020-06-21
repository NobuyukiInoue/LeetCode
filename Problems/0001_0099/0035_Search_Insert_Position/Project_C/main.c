#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "include/mylib.h"

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
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int *nums;
    int numsSize = ml_str_to_int_array(flds[0], &nums);
    int target = strtol(flds[1], NULL, 10);

    ml_print_int_array("nums", nums, numsSize);
    printf("target = %d\n", target);

    clock_t time_start = clock();

    int results = searchInsert(nums, numsSize, target);

    clock_t time_end = clock();

    // result print.
    printf("result = %d\n", results);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

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
