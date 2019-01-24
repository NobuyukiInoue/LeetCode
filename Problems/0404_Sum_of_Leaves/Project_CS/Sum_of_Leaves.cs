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
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();
        string[] nums1 = flds.Split(',');

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_node(nums1, 0, 0);
        Console.WriteLine("root = \n" + ope_t.output(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = SumOfLeftLeaves(root);
        Console.WriteLine("result = " + result.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
