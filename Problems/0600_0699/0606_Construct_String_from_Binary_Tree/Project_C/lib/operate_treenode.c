#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../include/mylib.h"
#include "../include/treenode.h"
#include "../include/operate_treenode.h"

struct TreeNode *createTreeNode(char *flds)
{
    char *nums[65535];

    int nums_length = ml_split(flds, ",", nums, sizeof(nums)/sizeof(nums[0]));
    nums[nums_length] = NULL;

    return createSubTreeNode(nums, nums_length, 0, 0);
}

struct TreeNode *createSubTreeNode(char *flds[], int flds_length, int depth, int pos)
{
    if (flds_length == 0)
        return NULL;

    int cur_pos = 0;
    for (int i = 0; i < depth; ++i)
        cur_pos += (int)pow(2, i);
    
    if (cur_pos + pos > flds_length - 1)
        return NULL;
    
    if (strcmp(flds[cur_pos + pos], "null") == 0)
        return NULL;

    struct TreeNode *node = malloc(sizeof(struct TreeNode));
    node->val = strtol(flds[cur_pos + pos], NULL, 10);
    node->left = createSubTreeNode(flds, flds_length, depth + 1, 2*pos);
    node->right = createSubTreeNode(flds, flds_length, depth + 1, 2*pos + 1);

    return node;
}

#define MAX_STAIR_DEPTH     256
#define MAX_STRING_LENGTH   1024

char* tree_to_staircase_string(struct TreeNode *node) {
    char *resultList[MAX_STAIR_DEPTH];

    for (int i = 0; i < MAX_STAIR_DEPTH; ++i) {
        resultList[i] = malloc(sizeof(char)*MAX_STRING_LENGTH);
        resultList[i][0] = '\0';
    }

    tree_to_staircase_substring(node, resultList, 0);

    char* resultStr;
    int resultStr_length = 0;

    for (int i = 0; i < MAX_STAIR_DEPTH && resultList[i][0] != '\0'; ++i) {
        resultStr_length += strlen(resultList[i]) + 1;  // prefix '\n'
    }
    resultStr_length++;     // prefix '\0'

    resultStr = malloc(sizeof(char)*resultStr_length);
    resultStr[0] = '\0';

    for (int i = 0; i < MAX_STAIR_DEPTH && resultList[i][0] != '\0'; ++i) {
        strcat(resultStr, resultList[i]);
        strcat(resultStr, "\n");
    }
    resultStr[resultStr_length - 1] = '\0';

    return resultStr;
}

void tree_to_staircase_substring(struct TreeNode *node, char *resultList[], int n) {
    if (node == NULL)
        return;
    
    char val_to_str[MAX_STRING_LENGTH];

    if (resultList[n][0] == '\0') {
        sprintf(val_to_str, "(%d)", node->val);
    } else {
        sprintf(val_to_str, ",(%d)", node->val);
    }

    strcat(resultList[n], val_to_str);
    
    if (node->left != NULL) {
        tree_to_staircase_substring(node->left, resultList, n + 1);
    }
    if (node->right != NULL) {
        tree_to_staircase_substring(node->right, resultList, n + 1);
    }
}

char* tree2str(struct TreeNode *t) {
    if (t == NULL)
        return "";

    char *resultStr = NULL;

    if (t->left == NULL && t->right == NULL) {
        resultStr = calloc(10, sizeof(char));
        sprintf(resultStr, "%d", t->val);

    } else if (t->left != NULL && t->right == NULL) {
        char *resultStr_left = tree2str(t->left);
        resultStr = calloc(strlen(resultStr_left) + 10, sizeof(char));
        sprintf(resultStr, "%d(%s)", t->val, resultStr_left);

    } else if(t->left == NULL && t->right != NULL) {
        char *resultStr_right = tree2str(t->right);
        resultStr = calloc(strlen(resultStr_right) + 10, sizeof(char));
        sprintf(resultStr, "%d()(%s)", t->val, resultStr_right);

    } else if(t->left != NULL && t->right != NULL) {
        char *resultStr_left = tree2str(t->left);
        char *resultStr_right = tree2str(t->right);
        resultStr = calloc(strlen(resultStr_left) + strlen(resultStr_right) + 10, sizeof(char));
        sprintf(resultStr, "%d(%s)(%s)", t->val, resultStr_left, resultStr_right);

    }

    return resultStr;
}
