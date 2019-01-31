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
char* tree2str(struct TreeNode* t);

struct TreeNode *set_node(char *flds[], int flds_length, int depth, int pos);
void output_tree(struct TreeNode *node);
void output_node(struct TreeNode *node, char *resultStr[], int n);
void str_replace(const char *src, const char *target, const char *replace, char **result);
int loop_main(char *arg);

#define MAX_RESULT_SIZE 65535

char* tree2str(struct TreeNode* t) 
{
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
    char *flds[MAX_RESULT_SIZE];

    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");

    int flds_length = split(arg, ",", flds, sizeof(flds)/sizeof(flds[0]));
    struct TreeNode *t = set_node(flds, flds_length, 0, 0);

    printf("t = \n");
    output_tree(t);

    clock_t time_start = clock();

    char* result = tree2str(t);

    clock_t time_end = clock();

    printf("result = %s\n", result);
    printf("Execute time ... %.0f ms\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // char* result free().
    free(result);

    // char* flds[] free().
    p_char_array_free(flds, flds_length);

    return 0;
}

int main(int argc, char *argv[])
{
    FILE *fp;
    char str[MAX_RESULT_SIZE];

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

    while((fgets(str, MAX_RESULT_SIZE - 1, fp)) != NULL) {
        printf("arg = %s\n", str);
        loop_main(str);
    }

    fclose(fp);
    return 0;
}