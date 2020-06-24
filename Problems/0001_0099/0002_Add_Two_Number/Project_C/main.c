#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "include/mylib.h"
#include "include/listnode.h"
#include "include/operate_listnode.h"

/* Function prototype declaration */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2);


int loop_main(char* arg);

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

int loop_main(char* arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char* flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int *nums1;
    int *nums2;
    int nums1_length = ml_str_to_int_array(flds[0], &nums1);
    int nums2_length = ml_str_to_int_array(flds[1], &nums2);
    ml_print_int_array("nums1", nums1, nums1_length);
    ml_print_int_array("nums2", nums2, nums2_length);

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

    // int nums1[], nums2[] clear.
    if (nums2 != NULL) {
        free(nums2);
    }
    if (nums1 != NULL) {
        free(nums1);
    }

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
