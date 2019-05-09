#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../mylib_C/mylib.h"

/* Definition for a binary tree node.*/
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/* Function prototype declaration */
struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2);
struct TreeNode *set_node(char *flds[], int flds_length, int depth, int pos);
void output_tree(struct TreeNode *node);
void output_node(struct TreeNode *node, char *resultStr[], int n);
char* tree2str(struct TreeNode* t);
int loop_main(char *arg);


struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2)
{
    if (t1 == NULL && t2 == NULL) {
        return NULL;
    } else if (t1 != NULL && t2 != NULL) {
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = t1->val + t2->val;
        node->left = mergeTrees(t1->left, t2->left);
        node->right = mergeTrees(t1->right, t2->right);
        return node;
    } else if (t1 != NULL) {
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = t1->val;
        node->left = mergeTrees(t1->left, NULL);
        node->right = mergeTrees(t1->right, NULL);
        return node;
    } else if (t2 != NULL) {
        struct TreeNode* node = (struct TreeNode*)malloc(sizeof(struct TreeNode));
        node->val = t2->val;
        node->left = mergeTrees(NULL, t2->left);
        node->right = mergeTrees(NULL, t2->right);
        return node;
    } else {
        return NULL;
    }
}

struct TreeNode *set_node(char *flds[], int flds_length, int depth, int pos)
{
    if ( flds_length == 0)
        return NULL;

    int cur_pos = 0;
    for (int i = 0; i < depth; ++i)
        cur_pos += (int)pow(2, i);
    
    if (cur_pos + pos > flds_length - 1)
        return NULL;
    
    if (strcmp(flds[cur_pos + pos], "NULL") == 0)
        return NULL;

    struct TreeNode *node = malloc(sizeof(struct TreeNode));
    node->val = strtol(flds[cur_pos + pos], NULL, 10);
    node->left = set_node(flds, flds_length, depth + 1, 2*pos);
    node->right = set_node(flds, flds_length, depth + 1, 2*pos + 1);

    return node;
}

#define MAX_DEPTH   256
#define MAX_LENGTH  1024

void output_tree(struct TreeNode *node)
{
    char *resultStr[MAX_DEPTH];

    for (int i = 0; i < MAX_DEPTH; ++i) {
        resultStr[i] = malloc(sizeof(char)*MAX_LENGTH);
        resultStr[i][0] = '\0';
    }

    output_node(node, resultStr, 0);

    for (int i = 0; i < MAX_DEPTH && resultStr[i][0] != '\0'; ++i)
        printf("%s\n", resultStr[i]);
}

void output_node(struct TreeNode *node, char *resultStr[], int n)
{
    if (node == NULL)
        return;
    
    char val_to_str[MAX_LENGTH];
    if (resultStr[n][0] == '\0')
        sprintf(val_to_str, "(%d)", node->val);
    else
        sprintf(val_to_str, ",(%d)", node->val);

    strcat(resultStr[n], val_to_str);
    
    if (node->left != NULL) {
        output_node(node->left, resultStr, n + 1);
    }
    if (node->right != NULL) {
        output_node(node->right, resultStr, n + 1);
    }
}

char* tree2str(struct TreeNode* t) 
{
#define MAX_RESULT_SIZE 65535

    char* resultStr = (char*)malloc(sizeof(char)*MAX_RESULT_SIZE);
    resultStr[0] = '\0';

    if (t == NULL)
        return resultStr;

    sprintf(resultStr, "%d", t->val);

    if (t->left == NULL && t->right == NULL)
        return resultStr;

    char* p = tree2str(t->left);
    strcat(resultStr, "(");
    if (*p != '\0')
        strcat(resultStr, p);
    strcat(resultStr, ")");
    free(p);

    if (t->right != NULL) {
        char* p = tree2str(t->right);
        strcat(resultStr, "(");
        if (*p != '\0')
            strcat(resultStr, p);
        strcat(resultStr, ")");
        free(p);
    }

    if (strlen(resultStr) >= MAX_RESULT_SIZE)
        err_exit("resultStr size Error!\n");

    return resultStr;
}

int loop_main(char *arg)
{
    char *flds[2];
    char *nums1[1024];
    char *nums2[1024];

    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");

    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int nums1_length = split(flds[0], ",", nums1, sizeof(nums1)/sizeof(nums1[0]));
    nums1[nums1_length] = NULL;

    int nums2_length = split(flds[1], ",", nums2, sizeof(nums2)/sizeof(nums2[0]));
    nums2[nums2_length] = NULL;

    struct TreeNode *t1 = set_node(nums1, nums1_length, 0, 0);
    struct TreeNode *t2 = set_node(nums2, nums2_length, 0, 0);

    printf("t1 = \n");
    output_tree(t1);
    printf("t2 = \n");
    output_tree(t2);

    clock_t time_start = clock();

    struct TreeNode* result = mergeTrees(t1, t2);

    clock_t time_end = clock();
    printf("result = \n");
    output_tree(result);
    printf("result = %s\n", tree2str(result));
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // struct TreeNode* result free()
    free(result);

    // struct TreeNode* t1, t2 free()
    free(t2);
    free(t1);

    // char* nums2[] free().
    p_char_array_free(nums2, nums2_length);

    // char* nums1[] free().
    p_char_array_free(nums1, nums1_length);

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
