using System;

public class Solution
{
    public int PathSum(TreeNode root, int sum)
    {
        if(root == null)
            return 0;
        return includeRoot(root, sum) + PathSum(root.left, sum) + PathSum(root.right, sum);
    }

    public int includeRoot(TreeNode root, int sum)
    {
        if (root == null)
            return 0;
        if (root.val == sum)
            return 1 + includeRoot(root.left, sum - root.val) + includeRoot(root.right, sum - root.val);
        else
            return includeRoot(root.left, sum - root.val) + includeRoot(root.right, sum - root.val);
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode node = ope_t.CreateTreeNode(flds[0]);
        Console.Write("node = \n" + ope_t.TreeToStaircaseString(node));
        Console.WriteLine("node = " + ope_t.Tree2str(node));
        int sum = int.Parse(flds[1]);
        Console.WriteLine("sum = " + sum.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = PathSum(node, sum);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
