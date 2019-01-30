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
    public int DiameterOfBinaryTree(TreeNode root)
    {
        if (root == null)
            return 0;
        int fnode = 0;
        return RecursiveDiameter(root, ref fnode);
    }

    public int RecursiveDiameter(TreeNode node,ref int fnode)
    {
        if (node == null)
        {
            fnode = 0;
            return 0;
        }
        
        if (node.left == null && node.right == null)
        {
            fnode = 0;
            return 0;
        }
       
        int ldist = 0;
        int rdist = 0;
        
        int ldm = RecursiveDiameter(node.left,ref ldist);
        int rdm = RecursiveDiameter(node.right,ref rdist);
                
        fnode = Math.Max(ldist, rdist) + 1;
        int diameter = ldist + rdist;
        if (node.left != null)
        {
            diameter++;
        }
        if (node.right != null)
        {
            diameter++;
        }
        return Math.Max(diameter, Math.Max(ldm, rdm));
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

        int result = DiameterOfBinaryTree(root);
        Console.WriteLine("result = " + result.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
