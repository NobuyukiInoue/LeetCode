#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "../../../mylib_C/mylib.h"

/* Definition for a binary tree node.*/
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/* Function prototype declaration */
bool isSubtree(struct TreeNode* s, struct TreeNode* t);
bool isSameTree(struct TreeNode*, struct TreeNode*);
struct TreeNode *set_node(char *flds[], int flds_length, int depth, int pos);
void output_tree(struct TreeNode *node);
void output_node(struct TreeNode *node, char *resultStr[], int n);
void str_replace(const char *src, const char *target, const char *replace, char **result);
int loop_main(char *arg);

bool isSubtree(struct TreeNode* s, struct TreeNode* t)
{
    if (s->val == t->val)
        if (isSameTree(s, t))
            return true;
    if (s->left != NULL)
        if (isSubtree(s->left, t))
            return true;
    if (s->right != NULL)
        if (isSubtree(s->right, t))
            return true;
    return false;
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q)
{
    if(p && q)
        return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    else if(p == NULL && q == NULL)
        return true;
    else
        return false;
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
    
    if (strcmp(flds[cur_pos + pos], "null") == 0)
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

int loop_main(char *arg)
{
    char *flds[2];
    char *nums1[256];
    char *nums2[256];

    replace(arg, "[[", "");
    replace(arg, "]]", "");
    replace(arg, "\n", "");

    int flds_length = split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    int nums1_length = split(flds[0], ",", nums1, sizeof(nums1)/sizeof(nums1[0]));
    nums1[nums1_length] = NULL;

    int nums2_length = split(flds[1], ",", nums2, sizeof(nums2)/sizeof(nums2[0]));
    nums2[nums2_length] = NULL;

    struct TreeNode *s = set_node(nums1, nums1_length, 0, 0);
    struct TreeNode *t = set_node(nums2, nums2_length, 0, 0);

    printf("s = \n");
    output_tree(s);
    printf("t = \n");
    output_tree(t);

    clock_t time_start = clock();

    bool result = isSubtree(s, t);

    clock_t time_end = clock();

    if (result)
        printf("result = true\n");
    else
        printf("result = false\n");

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);


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
