using System;
using System.Collections.Generic;

// Definition for a binary tree node.
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x)
    {
        val = x; 
    }
}

public class Solution {
    public bool IsUnivalTree(TreeNode root)
    {
        if (root == null)
            return false;

        return isTree_SameVal(root, root.val);
    }

    public bool isTree_SameVal(TreeNode node, int val)
    {
        if (node.val != val)
            return false;
        if (node.left != null)
            if (isTree_SameVal(node.left, val) == false)
                return false;
        if (node.right != null)
            if (isTree_SameVal(node.right, val) == false)
                return false;
        
        return true;
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
        TreeNode root = ope_t.set_TreeNode(flds);
        Console.Write("node =\n" + ope_t.output_TreeNode(root));
        Console.WriteLine("node = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsUnivalTree(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString() );
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
