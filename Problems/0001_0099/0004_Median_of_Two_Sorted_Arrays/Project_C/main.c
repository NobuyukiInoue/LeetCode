#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "include/mylib.h"

/* Function prototype declaration */
double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size);
static int compareInt(const void* a, const void* b);
void sort(int nums[], int length);


int loop_main(char* arg);


double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    int all_nums_length = nums1Size + nums2Size;
    int *all_nums = malloc(sizeof(int)*all_nums_length);
    int i, j;

    for (i = 0; i < nums1Size; ++i)
        all_nums[i] = nums1[i];

    for (j = 0; j < nums2Size; ++j)
        all_nums[i + j] = nums2[j];

    //sort(all_nums, all_nums_length);
    qsort(all_nums, all_nums_length, sizeof(int), compareInt);

    if (all_nums_length % 2 == 1)
        return (double)all_nums[all_nums_length / 2];
    else
        return (double)(all_nums[all_nums_length / 2 - 1] + all_nums[all_nums_length / 2])/2.0;
}

static int compareInt(const void* a, const void* b)
{
    int aNum = *(int*)a;
    int bNum = *(int*)b;

    return aNum - bNum;
}

/*
void sort(int nums[], int nums_length)
{
    int i, j, tmp;

    for (i = 0; i < nums_length; ++i) {
        for (j = i + 1; j < nums_length; ++j) {
            if (nums[i] > nums[j]) {
                tmp =  nums[i];
                nums[i] = nums[j];
                nums[j] = tmp;
            }
        }
    }
}
*/

int loop_main(char* arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int *nums1, *nums2;
    int nums1_length = ml_str_to_int_array(flds[0], &nums1);
    int nums2_length = ml_str_to_int_array(flds[1], &nums2);
    ml_print_int_array("nums1", nums1, nums1_length);
    ml_print_int_array("nums2", nums2, nums2_length);

    clock_t time_start = clock();

    double result = findMedianSortedArrays(nums1, nums1_length, nums2, nums2_length);

    clock_t time_end = clock();

    printf("result = %f\n", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // nums1[], nums2[] free().
    free(nums2);
    free(nums1);

    // char* flds[] clear.
    ml_p_char_array_free(flds, flds_length);
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
