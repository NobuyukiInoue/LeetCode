using System;

public class Solution
{
    public bool isSymmetric(TreeNode root)
    {
        if (root == null)
            return true;
        return checkSymmetric(root.left, root.right);
    }

    public bool checkSymmetric(TreeNode temp1, TreeNode temp2)
    {
        if (temp1 == null && temp2 == null)
            return true;
        if (temp1 == null || temp2 == null)
            return false;
        if (temp1.val != temp2.val)
            return false;
        return ( checkSymmetric(temp1.left, temp2.right) && checkSymmetric(temp1.right, temp2.left) );
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.CreateTreeNode(flds);

        Console.Write("root = \n" + ope_t.TreeToStaircaseString(root));
        Console.WriteLine("root = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = isSymmetric(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
