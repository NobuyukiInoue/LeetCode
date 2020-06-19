using System;

public class Solution {
    public bool HasPathSum(TreeNode root, int sum)
    {
        if (root == null)
            return false;

        if ((root.left == null) && (root.right == null))
            if (root.val == sum)
                return true;
            else
                return false;

        if (root.left != null)
            if (HasPathSum(root.left, sum - root.val))
                return true;

        if (root.right != null)
            if (HasPathSum(root.right, sum - root.val))
                return true;

        return false;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.CreateTreeNode(flds[0]);
        Console.Write("root = \n" + ope_t.TreeToStaircaseString(root));
        Console.WriteLine("root = " + ope_t.Tree2str(root));
        int sum = int.Parse(flds[1]);
        Console.WriteLine("sum = " + sum.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result =  HasPathSum(root, sum);

        sw.Stop();
        Console.WriteLine("Result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
