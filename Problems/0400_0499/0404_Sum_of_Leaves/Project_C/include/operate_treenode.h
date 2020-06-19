struct TreeNode *createTreeNode(char *flds);
struct TreeNode *createSubTreeNode(char *flds[], int flds_length, int depth, int pos);
char* tree_to_staircase_string(struct TreeNode *node);
void tree_to_staircase_substring(struct TreeNode *node, char *resultStr[], int n);
char* tree2str(struct TreeNode *t);
