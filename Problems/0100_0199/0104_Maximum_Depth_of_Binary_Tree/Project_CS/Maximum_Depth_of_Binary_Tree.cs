using System;

public class Solution
{
    public int MaxDepth(TreeNode root)
    {
        if (root == null)
            return 0;

        int max_l = 0, max_r = 0;
        if (root.left != null)
            max_l = MaxDepth(root.left);
        if (root.right != null)
            max_r = MaxDepth(root.right);
        if (max_l >= max_r)
            return max_l + 1;
        else
            return max_r + 1;   
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

        int result = MaxDepth(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString() );
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
