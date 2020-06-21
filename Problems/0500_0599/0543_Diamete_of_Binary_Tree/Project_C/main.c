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
int DiameterOfBinaryTree(struct TreeNode* root);
int RecursiveDiameter(struct TreeNode* root, int* fnode);
#define max(x,y) ((x)>(y)?(x):(y))

int loop_main(char *arg);


int DiameterOfBinaryTree(struct TreeNode* root)
{
    if (root == NULL)
        return 0;
    int fnode = 0;
    return RecursiveDiameter(root, &fnode);
}

int RecursiveDiameter(struct TreeNode* root, int* fnode)
{
    if (root == NULL)
    {
        *fnode = 0;
        return 0;
    }
    
    if (root->left == NULL && root->right == NULL)
    {
        *fnode = 0;
        return 0;
    }
    
    int ldist = 0;
    int rdist = 0;
    
    int ldm = RecursiveDiameter(root->left, &ldist);
    int rdm = RecursiveDiameter(root->right, &rdist);

    *fnode = max(ldist, rdist) + 1;
    int diameter = ldist + rdist;
    if (root->left != NULL)
    {
        diameter++;
    }
    if (root->right != NULL)
    {
        diameter++;
    }
    return max(diameter, max(ldm, rdm));
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

    int result = DiameterOfBinaryTree(root);

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
