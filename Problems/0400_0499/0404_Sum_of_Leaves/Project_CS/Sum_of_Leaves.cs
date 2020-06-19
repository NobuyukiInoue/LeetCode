using System;

public class Solution
{
    public int SumOfLeftLeaves(TreeNode root)
    {
        if (root == null)
            return 0;
        int sum = 0;
        if (root.left != null)
            if (root.left.left == null && root.left.right == null)
                sum += root.left.val;
            else
                sum += sub_sumOfLeftLeaves(root.left);
        if (root.right != null)
            sum += sub_sumOfLeftLeaves(root.right);
        return sum;
    }
    
    public int sub_sumOfLeftLeaves(TreeNode node)
    {
        int sum = 0;
        if (node.left != null)
            if (node.left.left == null && node.left.right == null)
                sum = node.left.val;
            else
                sum += sub_sumOfLeftLeaves(node.left);
        if (node.right != null)
            sum += sub_sumOfLeftLeaves(node.right);
        return sum;
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

        int result = SumOfLeftLeaves(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
