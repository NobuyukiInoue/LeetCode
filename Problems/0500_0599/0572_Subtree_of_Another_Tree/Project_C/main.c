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
bool isSubtree(struct TreeNode* s, struct TreeNode* t);
bool isSameTree(struct TreeNode*, struct TreeNode*);

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

int loop_main(char *arg)
{
    ml_replace(arg, "[[", "");
    ml_replace(arg, "]]", "");
    ml_replace(arg, "\n", "");

    char *flds[2];
    int flds_length = ml_split(arg, "],[", flds, sizeof(flds)/sizeof(flds[0]));

    struct TreeNode *s = createTreeNode(flds[0]);
    struct TreeNode *t = createTreeNode(flds[1]);

    char *resultStr;
    resultStr = tree_to_staircase_string(s);
    printf("s = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(s);
    printf("s = %s\n", resultStr);
    free(resultStr);

    resultStr = tree_to_staircase_string(t);
    printf("t = \n%s", resultStr);
    free(resultStr);

    resultStr = tree2str(t);
    printf("t = %s\n", resultStr);
    free(resultStr);

    clock_t time_start = clock();

    bool result = isSubtree(s, t);

    clock_t time_end = clock();

    if (result)
        printf("result = true\n");
    else
        printf("result = false\n");

    printf("Execute time ... %.0f ms\n\n", 1000*(double)(time_end - time_start)/CLOCKS_PER_SEC);

    // struct treenode s, t clear.
    free(t);
    free(s);

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
