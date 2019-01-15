#include <stdio.h>
#include <stdlib.h>

/**
 * Definition for a binary tree node.
*/
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

bool isSameTree(struct TreeNode* p, struct TreeNode* q)
{
    if(p && q)
        return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    else if(p == NULL && q == NULL)
        return true;
    else
        return false;
}


TreeNode set_node(char[] data)
{
    if (data.Length == 0) {
        return null;
    }

    TreeNode new_node = new TreeNode(int.Parse(data[0]));
    if (data[1] != "null") {
        new_node.left = new TreeNode(int.Parse(data[1]));
    }
    if (data[2] != "null") {
        new_node.right = new TreeNode(int.Parse(data[2]));
    }

    return new_node;
}

private string output_node(TreeNode node)
{
    string tempStr = "";

    if (node != null) {
        tempStr += node.val + ",";
    }
    if (node.left != null) {
        tempStr += node.left.val + ",";
    }
    else {
        tempStr += "null,";
    }
    if (node.right != null) {
        tempStr += node.right.val;
    }
    else
    {
        tempStr += "null";
    }

    return tempStr;
}

int split( char *str, const char *delim, char *outlist[] ) {
    char    *tk;
    int     cnt = 0;

    tk = strtok( str, delim );
    while( tk != NULL && cnt < MAXITEM ) {
        outlist[cnt++] = tk;
        tk = strtok( NULL, delim );
    }
    return cnt;
}

void main(int argc, *char[] argv)
{
    int i;
    printf("args = ");
    for (i = 0; i < argc; ++i)
        print("%s", argv[i]);

//    string[] workStr = args.Split('\t');
    string[] workStr = args.split((char)0x09);    // [TAB]

    string[] arg1 = workStr[0].Split(',');
    string[] arg2 = workStr[1].Split(',');

    TreeNode p = set_node(arg1);
    TreeNode q = set_node(arg2);

    Console.WriteLine("p = " + output_node(p));
    Console.WriteLine("q = " + output_node(q));

    System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
    sw.Start();

    Console.WriteLine("result = " + IsSameTree(p, q).ToString() );

    sw.Stop();
    Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
}
