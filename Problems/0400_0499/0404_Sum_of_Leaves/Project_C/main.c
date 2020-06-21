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
int sumOfLeftLeaves(struct TreeNode* root);
int sub_sumOfLeftLeaves(struct TreeNode* node);

int loop_main(char *arg);


int sumOfLeftLeaves(struct TreeNode* root)
{
    if (root == NULL)
        return 0;
    int sum = 0;
    if (root->left != NULL) {
        if (root->left->left == NULL && root->left->right == NULL)
            sum += root->left->val;
        else
            sum += sub_sumOfLeftLeaves(root->left);
    }
    if (root->right != NULL)
        sum += sub_sumOfLeftLeaves(root->right);
    return sum;
}

int sub_sumOfLeftLeaves(struct TreeNode* node)
{
    int sum = 0;
    if (node->left != NULL) {
        if (node->left->left == NULL && node->left->right == NULL)
            sum = node->left->val;
        else
            sum += sub_sumOfLeftLeaves(node->left);
    }
    if (node->right != NULL)
        sum += sub_sumOfLeftLeaves(node->right);
    return sum;
}

int loop_main(char *arg)
{
    ml_replace(arg, "[", "");
    ml_replace(arg, "]", "");
    ml_replace(arg, "\n", "");

    char *flds = arg;
    struct TreeNode *root = createTreeNode(flds);

    char *resultStr;
    resultStr = tree_to_staircase_string(root);
    printf("root = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(root);
    printf("root = %s\n", resultStr);
    free(resultStr);

    clock_t time_start = clock();

    int result = sumOfLeftLeaves(root);

    clock_t time_end = clock();

    printf("result = %d\n", result);
    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // struct treenode root clear.
    free(root);

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
        printf("args = %s\n", line);
        loop_main(line);
    }

    fclose(fp);
    return 0;
}
