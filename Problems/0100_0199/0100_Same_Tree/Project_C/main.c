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
bool isSameTree(struct TreeNode*, struct TreeNode*);

int loop_main(char *arg);


bool isSameTree(struct TreeNode* p, struct TreeNode* q)
{
    if(p && q)
        return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    else if(p == NULL && q == NULL)
        return true;
    else
        return false;
}

int loop_main(char *arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char *flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    struct TreeNode *p = createTreeNode(flds[0]);
    struct TreeNode *q = createTreeNode(flds[1]);

    char *resultStr;
    resultStr = tree_to_staircase_string(p);
    printf("p = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(p);
    printf("p = %s\n", resultStr);
    free(resultStr);

    resultStr = tree_to_staircase_string(q);
    printf("q = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(q);
    printf("q = %s\n", resultStr);
    free(resultStr);

    clock_t time_start = clock();

    bool result = isSameTree(p, q);

    clock_t time_end = clock();

    if (result)
        printf("result = true\n");
    else
        printf("result = false\n");

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // strunct TreeNode *p. *t clear.
    // printf("treenode_free(q) ... %d\n", treenode_free(q));
    // printf("treenode_free(p) ... %d\n", treenode_free(p));
    treenode_free(q);
    treenode_free(p);

    // char* flds[] free().
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
