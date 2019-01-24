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
    public TreeNode ConvertBST(TreeNode root)
    {
        TreeNode node = root;
        Stack<TreeNode> stack = new Stack<TreeNode>();

        int sum = 0;
        while (node != null || stack.Count > 0)
        {
            if (node != null)
            {
                stack.Push(node);
                node = node.right;
            }
            else
            {
                // visit
                node = stack.Pop();
                sum += node.val;
                node.val = sum;
                
                node = node.left;
            }
        }
        
        return root;
    }
    
    List<int> nums = new List<int>();
    public TreeNode ConvertBST_work(TreeNode root)
    {
        getAllVal(root);

        nums.Sort();
        nums.Reverse();

        TreeNode resultNode = root;
        setGreater(resultNode);

        return resultNode;
    }

    private void getAllVal(TreeNode node)
    {
        if (node == null)
            return;
        nums.Add(node.val);
        if (node.left != null)
            getAllVal(node.left);
        if (node.right != null)
            getAllVal(node.right);
    }

    public void setGreater(TreeNode node)
    {
        if (node == null)
            return;
        node.val += calc_addVal(node.val);
        if (node.left != null)
            setGreater(node.left);
        if (node.right != null)
            setGreater(node.right);
    }

    private int calc_addVal(int currentVal)
    {
        int addVal = 0;
        for (int i = 0; i < nums.Count; ++i)
            if (nums[i] > currentVal)
                addVal += nums[i];
            else
                break;
        
        return addVal;
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
        string[] flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim().Split(",");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_node(flds, 0, 0);
        Console.WriteLine("root = \n" + ope_t.output(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        TreeNode result = ConvertBST(root);
        Console.WriteLine("result = \n" + ope_t.output(result));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
