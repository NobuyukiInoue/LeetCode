using System;
using System.Collections.Generic;

// Definition for a binary tree node.
 public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

public class Solution
{
    public string Tree2str(TreeNode t)
    {
        if (t == null)
            return "";

        string resultStr = t.val.ToString();

        if (t.left == null && t.right == null)
            return resultStr;

        resultStr += "(" + Tree2str(t.left) + ")";
        if (t.right != null)
            resultStr += "(" + Tree2str(t.right) + ")";

        return resultStr;
    }

    public string output_int_array(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = nums[0].ToString();

        for (int i = 1; i < resultStr.Length; ++i)
        {
            resultStr += ", " + nums[i].ToString();
        }

        return resultStr;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim().Split(',');

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode t = ope_t.set_node(flds, 0, 0);
        Console.WriteLine("t = \n" + ope_t.output(t));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = Tree2str(t);

        sw.Stop();
        Console.WriteLine("result = " + result);
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
