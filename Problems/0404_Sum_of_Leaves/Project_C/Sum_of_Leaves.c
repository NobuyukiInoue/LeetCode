#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>

#include "mylib.h"

/* Definition for a binary tree node.*/
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

/* Function prototype declaration */
int sumOfLeftLeaves(struct TreeNode* root);
int sub_sumOfLeftLeaves(struct TreeNode* node);

struct TreeNode *set_node(char *flds[], int flds_length, int depth, int pos);
void output_tree(struct TreeNode *node);
void output_node(struct TreeNode *node, char *resultStr[], int n);
void str_replace(const char *src, const char *target, const char *replace, char **result);
int loop_main(char *arg);


int sumOfLeftLeaves(struct TreeNode* root)
{
    if (root == NULL)
        return 0;
    int sum = 0;
    if (root->left != NULL)
        if (root->left->left == NULL && root->left->right == NULL)
            sum += root->left->val;
        else
            sum += sub_sumOfLeftLeaves(root->left);
    if (root->right != NULL)
        sum += sub_sumOfLeftLeaves(root->right);
    return sum;
}
    
int sub_sumOfLeftLeaves(struct TreeNode* node)
{
    int sum = 0;
    if (node->left != NULL)
        if (node->left->left == NULL && node->left->right == NULL)
            sum = node->left->val;
        else
            sum += sub_sumOfLeftLeaves(node->left);
    if (node->right != NULL)
        sum += sub_sumOfLeftLeaves(node->right);
    return sum;
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
    
    if (flds[cur_pos + pos] == "null")
        return NULL;

    struct TreeNode *node = malloc(sizeof(struct TreeNode));
    node->val = strtol(flds[cur_pos + pos], NULL, 10);
    node->left = set_node(flds, flds_length, depth + 1, 2*pos);
    node->right = set_node(flds, flds_length, depth + 1, 2*pos + 1);

    return node;
}

void output_tree(struct TreeNode *node)
{
    char *resultStr[256];

    for (int i = 0; i < 256; ++i) {
        resultStr[i] = malloc(sizeof(char)*256);
        resultStr[i][0] = '\0';
    }

    output_node(node, resultStr, 0);

    for (int i = 0; i < 256 && resultStr[i][0] != '\0'; ++i)
        printf("%s\n", resultStr[i]);
}

void output_node(struct TreeNode *node, char *resultStr[], int n)
{
    if (node == NULL)
        return;
    
    char val_to_str[256];
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
    int argv_length = strlen(arg);
    char tempstr1[256];
    char tempstr2[256];
    char *flds[2];
    char *nums1[256];
    char *nums2[256];

    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");

    int flds_length = split(arg, ",", flds);
    struct TreeNode *root = set_node(flds, flds_length, 0, 0);

    printf("root = \n");
    clock_t time_start = clock();

    output_tree(root);

    clock_t time_end = clock();

    printf("result = %d\n", sumOfLeftLeaves(root));

    printf("Execute time ... %.0f ms\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char str[256];

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

    while((fgets(str, 256, fp)) != NULL) {
        printf("arg = %s\n", str);
        loop_main(str);
    }

    fclose(fp);
    return 0;
}