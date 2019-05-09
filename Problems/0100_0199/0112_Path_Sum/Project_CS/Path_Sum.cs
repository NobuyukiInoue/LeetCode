using System;

// Definition for a binary tree node.
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) {
        val = x;
    }
}

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
        string[] nums1 = flds[0].Split(',');
        int sum = int.Parse(flds[1]);

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(nums1);

        Console.Write("root = \n" + ope_t.output_TreeNode(root));
        Console.WriteLine("root = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result =  HasPathSum(root, sum);
        Console.WriteLine("Result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
