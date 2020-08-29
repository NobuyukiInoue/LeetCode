#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
#include <time.h>


#include "lib/mylib.h"
#include "lib/treenode.h"
#include "lib/operate_treenode.h"


/* Function prototype declaration */
struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2);

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

int loop_main(char *arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char *flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    struct TreeNode *t1 = createTreeNode(flds[0]);
    struct TreeNode *t2 = createTreeNode(flds[1]);

    char *resultStr;
    resultStr = tree_to_staircase_string(t1);
    printf("t1 = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(t1);
    printf("t1 = %s\n", resultStr);
    free(resultStr);

    resultStr = tree_to_staircase_string(t2);
    printf("t2 = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(t2);
    printf("t2 = %s\n", resultStr);
    free(resultStr);

    clock_t time_start = clock();

    struct TreeNode *result = mergeTrees(t1, t2);

    clock_t time_end = clock();

    resultStr = tree_to_staircase_string(result);
    printf("result = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(result);
    printf("result = %s\n", resultStr);
    free(resultStr);

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // struct treenode t1, t2 clear.
    free(t2);
    free(t1);

    // char* flds[] clear.
    ml_p_char_array_free(flds, flds_length);
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
