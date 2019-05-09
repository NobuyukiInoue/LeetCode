using System;
using System.Collections.Generic;
using System.Linq;

// Definition for a binary tree node.
 public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

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
        string[] root_str = flds[0].Split(',');

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode node = ope_t.set_TreeNode(root_str);
        Console.Write("node = \n" + ope_t.output_TreeNode(node));
        Console.WriteLine("node = " + ope_t.Tree2str(node));
        int sum = int.Parse(flds[1]);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("result = " + PathSum(node, sum) );

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
