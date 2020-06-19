using System;
using System.Collections.Generic;

public class Solution {
    public bool IsUnivalTree(TreeNode root)
    {
        if (root == null)
            return false;

        return isTree_SameVal(root, root.val);
    }

    public bool isTree_SameVal(TreeNode node, int val)
    {
        if (node.val != val)
            return false;
        if (node.left != null)
            if (isTree_SameVal(node.left, val) == false)
                return false;
        if (node.right != null)
            if (isTree_SameVal(node.right, val) == false)
                return false;
        
        return true;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.CreateTreeNode(flds);
        Console.Write("node =\n" + ope_t.TreeToStaircaseString(root));
        Console.WriteLine("node = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsUnivalTree(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
