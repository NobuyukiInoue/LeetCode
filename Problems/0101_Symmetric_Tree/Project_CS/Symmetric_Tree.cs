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

        bool result = isSymmetric(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
