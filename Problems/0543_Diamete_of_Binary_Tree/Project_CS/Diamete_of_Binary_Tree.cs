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

    private TreeNode set_node(string[] flds, int depth, int pos)
    {
        if (flds.Length == 0)
            return null;

        int cur_pos = 0;
        for (int i = 0; i < depth; ++i)
            cur_pos += (int)Math.Pow(2, i);
        
        if (cur_pos + pos > flds.Length - 1)
            return null;
        
        if (flds[cur_pos + pos] == "null")
            return null;

        TreeNode node = new TreeNode(int.Parse(flds[cur_pos + pos]));
        node.left = set_node(flds, depth + 1, 2*pos);
        node.right = set_node(flds, depth + 1, 2*pos + 1);

        return node;
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

        TreeNode root = set_node(nums1, 0, 0);
        Output_TreeNode ot = new Output_TreeNode();

        Console.WriteLine("root = \n" + ot.output(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = DiameterOfBinaryTree(root);
        Console.WriteLine("result = " + result.ToString());

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}

public class Output_TreeNode
{
    List<string> resultStr;
    public string output(TreeNode node)
    {
        resultStr = new List<string>();

        output_tree(node, 0);
        return print_result();
    }
    public void output_tree(TreeNode node, int n)
    {
        if (node == null)
            return;
        
        if (resultStr.Count <= n)
            resultStr.Add("(" + node.val.ToString() + ")");
        else
            resultStr[n] += ",(" + node.val.ToString() + ")";

        if (node.left != null)
            output_tree(node.left, n + 1);
        if (node.right != null)
            output_tree(node.right, n + 1);

        return;
    }

    public string print_result()
    {
        string outputStr = "";

        for (int i = 0; i < resultStr.Count; ++i)
        {
            outputStr += resultStr[i] + "\n";
        }

        resultStr = null;
        return outputStr;
    }
}
