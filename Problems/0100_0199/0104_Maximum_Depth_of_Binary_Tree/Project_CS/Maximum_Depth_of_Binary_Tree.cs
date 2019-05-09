using System;

// Definition for a binary tree node.
 public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

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
        string[] nums = flds.Split(',');

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(nums);

        Console.Write("root = \n" + ope_t.output_TreeNode(root));
        Console.WriteLine("root = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = MaxDepth(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString() );
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
