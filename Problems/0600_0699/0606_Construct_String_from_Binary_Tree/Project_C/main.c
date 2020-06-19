#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>


#include "include/mylib.h"
#include "include/treenode.h"
#include "include/operate_treenode.h"


/* Function prototype declaration */
char* tree2str(struct TreeNode* t);

int loop_main(char *arg);


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

int loop_main(char *arg)
{
    char *flds;
    char *nums1[256];
    char *nums2[256];

    replace(arg, "[", "");
    replace(arg, "]", "");
    replace(arg, "\n", "");
    flds = arg;

    struct TreeNode *root = createTreeNode(flds);

    char *resultStr;
    resultStr = tree_to_staircase_string(root);
    printf("root = \n%s", resultStr);
    free(resultStr);

    clock_t time_start = clock();

    resultStr = tree2str(root);
    printf("result = %s\n", resultStr);
    free(resultStr);

    clock_t time_end = clock();

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

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
        printf("args = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
