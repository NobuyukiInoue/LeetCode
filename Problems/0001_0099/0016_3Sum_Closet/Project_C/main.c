#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#include "include/mylib.h"

/* Function prototype declaration */
int comparefn( const void* a, const void* b);
int threeSumClosest(int* nums, int numsSize, int target);


int loop_main(char* arg);

#define ABS(x) ((x)<0?-(x):(x))

int comparefn( const void* a, const void* b)
{
     int int_a = * ( (int*) a );
     int int_b = * ( (int*) b );

     if ( int_a == int_b ) return 0;
     else if ( int_a < int_b ) return -1;
     else return 1;
}

int threeSumClosest(int* nums, int numsSize, int target)
{
    // sort the array
    qsort(nums, numsSize, sizeof(int), comparefn);
    int i, j, k, diff, min_diff = INT_MAX;
    for(i = 0 ; i < numsSize ; i++)
    {
        j = i + 1;
        k = numsSize - 1;
        while(j < k)
        {
            diff = nums[i] + nums[j] + nums[k] - target;
            //temp = ABS(temp);
            if(diff == 0)
            {
                return target;
            }
            else
            {
                if(ABS(diff) < ABS(min_diff))
                {
                    min_diff = diff;
                }
                if(diff < 0)
                {// increase value
                    j++;
                }
                else//>0
                {
                    k--;
                }
            }
        }
    }
    return target + min_diff;
}

int loop_main(char* arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int *nums;
    int nums_length = ml_str_to_int_array(flds[0], &nums);
    ml_print_int_array("nums", nums, nums_length);

    int target = strtol(flds[1], NULL, 10);
    printf("target = %d\n", target);

    clock_t time_start = clock();

    int result =  threeSumClosest(nums, nums_length, target);

    clock_t time_end = clock();

    // result print.
    printf("results = %d\n", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // nums[] free().
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
