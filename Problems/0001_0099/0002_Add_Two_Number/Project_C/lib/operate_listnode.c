#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#include "../include/listnode.h"
#include "../include/operate_listnode.h"

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
