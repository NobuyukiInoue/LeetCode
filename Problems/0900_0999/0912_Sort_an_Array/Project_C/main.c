#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "lib/mylib.h"

/* Function prototype declaration */
int* sortArray(int* nums, int numsSize, int* returnSize);
int partition(int* nums, int left, int right);
void quicksort(int* nums, int left, int right);

static int compareInt(const void* a, const void* b);

int loop_main(char* arg);


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* sortArray(int* nums, int numsSize, int* returnSize){
    // 64ms
    quicksort(nums, 0, numsSize - 1);
//  quicksort2(nums, 0, numsSize - 1);
    *returnSize = numsSize;
    return nums;
}

int partition(int* nums, int left, int right) {
    int pivot = nums[right];
    int start = left;
    int end = right - 1;
    int temp;
    while (start <= end) {
        if (nums[start] < pivot) {
            start++;
        } else if (nums[end] >= pivot) {
            end--;
        } else {
            temp = nums[start];
            nums[start] = nums[end];
            nums[end] = temp;
            start++;
            end--;
        }
    }
    temp = nums[start];
    nums[start] = nums[right];
    nums[right] = temp;
    return start;
}

void quicksort(int* nums, int left, int right) {
    if (left >= right)
        return;
    int pivot = partition(nums, left, right);
    quicksort(nums, left, pivot - 1);
    quicksort(nums, pivot + 1, right);
}

void quicksort2(int * num, int start, int end){
    if (start >= end)
        return;
    int temp = num[start];
    int i = start, k = end;
    while (i < k){
        for (k; num[k] >= temp && k > i; k--);
        num[i] = num[k];
        num[k] = temp;
        for (i; num[i] <= temp && i < k; i++);
        num[k] = num[i];
        num[i] = temp;
    }
    quicksort2(num, start, i-1);
    quicksort2(num, k+1, end);
}

int loop_main(char* arg)
{
    ml_replace(arg, "\"", "");
    ml_replace(arg, "[", "");
    ml_replace(arg, "]", "");
    ml_replace(arg, "\n", "");

    int *nums;
    int numsLength = ml_str_to_int_array(arg, &nums);
    ml_print_int_array("nums", nums, numsLength);
    int returnSize;

    clock_t time_start = clock();

    int* result = sortArray(nums, numsLength, &returnSize);

    clock_t time_end = clock();

    ml_print_int_array("result", result, returnSize);
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
