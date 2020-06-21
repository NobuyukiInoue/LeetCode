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
struct TreeNode* convertBST(struct TreeNode* root);
void helper(struct TreeNode* root, int *curr_sum);

int loop_main(char *arg);


struct TreeNode* convertBST(struct TreeNode* root)
{
    int curr_sum = 0;
    helper(root, &curr_sum);
    return root;
}

void helper(struct TreeNode* root, int *curr_sum)
{
    if (!root) {
        return;
    }

    //go right first as everything on right is greater than root
    helper(root->right, curr_sum);
    root->val = root->val + *curr_sum;
    *curr_sum = root->val;
    //now go left, everything on left is lesser than root
    helper(root->left, curr_sum);
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

    struct TreeNode *result = convertBST(root);

    clock_t time_end = clock();

    resultStr = tree_to_staircase_string(root);
    printf("result = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(root);
    printf("result = %s\n", resultStr);
    free(resultStr);

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
