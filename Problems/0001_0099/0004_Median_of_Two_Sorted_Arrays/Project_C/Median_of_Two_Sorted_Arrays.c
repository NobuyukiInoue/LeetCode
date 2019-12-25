#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../../mylib_C/mylib.h"

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
    char* flds[2];
    char* str_nums[256];
    int nums1[256], nums2[256];

    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");
    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int str_nums_length;
    str_nums_length = split(flds[0], ",", str_nums, sizeof(str_nums)/sizeof(str_nums[0]));

    if (sizeof(nums1)/sizeof(nums1[0]) < str_nums_length)
        err_exit("nums1[] size error.\n");

    int nums1_length = str_to_int_array(str_nums, nums1, str_nums_length);

    str_nums_length = split(flds[1], ",", str_nums, sizeof(str_nums)/sizeof(str_nums[0]));

    if (sizeof(nums2)/sizeof(nums2[0]) < str_nums_length)
        err_exit("nums2[] size error.\n");

    int nums2_length = str_to_int_array(str_nums, nums2, str_nums_length);

    int target = strtol(flds[1], NULL, 10);

    clock_t time_start = clock();
    double result = findMedianSortedArrays(nums1, nums1_length, nums2, nums2_length);
    clock_t time_end = clock();

    printf("result = %f\n", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* str_nums[] free().
    p_char_array_free(str_nums, str_nums_length);

    // char* flds[] free().
    p_char_array_free(flds, flds_length);
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
