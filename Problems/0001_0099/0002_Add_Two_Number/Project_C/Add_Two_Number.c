#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../../mylib_C/mylib.h"

/* Function prototype declaration */
int* twoSum(int* nums, int numsSize, int target);
int loop_main(char* arg);

/* Definition for singly-linked list. */
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    struct ListNode* dummyHead = (struct ListNode*)malloc(sizeof(struct ListNode));
    dummyHead->val = 0;
    dummyHead->next = NULL;
    struct ListNode* p = l1;
    struct ListNode* q = l2;
    struct ListNode* curr = dummyHead;
    int carry = 0;

    while (p != NULL || q != NULL)
    {
        int x = (p != NULL) ? p->val : 0;
        int y = (q != NULL) ? q->val : 0;
        int sum = carry + x + y;

        carry = sum / 10;
        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        curr->next->val = sum % 10;
        curr->next->next = NULL;
        curr = curr->next;

        if (p != NULL)
            p = p->next;
        if (q != NULL)
            q = q->next;
    }

    if (carry > 0)
    {
        curr->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        curr->next->val = carry;
        curr->next->next = NULL;
    }

    return dummyHead->next;
}

struct ListNode* set_nodes(int nums[], int nums_Size, int index)
{
    if (index >= nums_Size)
        return NULL;
    
    struct ListNode* node = (struct ListNode*)malloc(sizeof(struct ListNode));

    node->val = nums[index];
    node->next = set_nodes(nums, nums_Size, index + 1);

    return node;
}


char* output_nodes(struct ListNode* ll)
{
    #define resultStr_MAX_SIZE  1024

    char* resultStr = (char *)malloc(sizeof(char)*resultStr_MAX_SIZE);
    sprintf(resultStr, "%d", ll->val); 

    if (ll->next != NULL) {
        strcat(resultStr, " -> ");
        strcat(resultStr, output_nodes(ll->next));
    }

    return resultStr;
}

int ListNode_free(struct ListNode* ll)
{
    if (ll == NULL)
        return 0;
    
    int result = 0;

    if (ll->next != NULL) {
        result += ListNode_free(ll->next);
    }

    free(ll);
    result++;

    return result;
}

int loop_main(char* arg)
{
    #define nums_MAX_SIZE   256

    int argv_length = strlen(arg);
    char* flds[2];
    char* str_nums1[nums_MAX_SIZE];
    char* str_nums2[nums_MAX_SIZE];
    int nums1[nums_MAX_SIZE];
    int nums2[nums_MAX_SIZE];

    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");
    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));
    int str_nums1_length = split(flds[0], ",", str_nums1, sizeof(str_nums1)/sizeof(str_nums1[0]));
    int str_nums2_length = split(flds[1], ",", str_nums2, sizeof(str_nums2)/sizeof(str_nums2[0]));

    // int nums1[] size check.
    if (sizeof(nums1)/sizeof(nums1[0]) < str_nums1_length)
        err_exit("nums1[] size error.");

    // int nums2[] size check.
    if (sizeof(nums2)/sizeof(nums2[0]) < str_nums2_length)
        err_exit("nums2[] size error.");

    int nums1_length = str_to_int_array(str_nums1, nums1, str_nums1_length);
    int nums2_length = str_to_int_array(str_nums2, nums2, str_nums2_length);
    struct ListNode* l1 = set_nodes(nums1, nums1_length, 0);
    struct ListNode* l2 = set_nodes(nums2, nums2_length, 0);
    printf("l1 = %s\n", output_nodes(l1));
    printf("l2 = %s\n", output_nodes(l2));

    clock_t time_start = clock();
    struct ListNode* result = addTwoNumbers(l1, l2);
    clock_t time_end = clock();

    // result print.
    printf("result = %s\n", output_nodes(result));
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // struct ListNode *l1, *l2, *result clear.
    int ret_result = ListNode_free(result);
    int ret_l1 = ListNode_free(l2);
    int ret_l2 = ListNode_free(l1);

    // char* str_nums1[], str_nums2[] free().
    p_char_array_free(str_nums2, str_nums2_length);
    p_char_array_free(str_nums1, str_nums1_length);

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
