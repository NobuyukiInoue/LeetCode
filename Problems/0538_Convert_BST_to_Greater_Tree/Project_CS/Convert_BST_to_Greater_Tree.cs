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
        string[] flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim().Split(",");

        TreeNode root = set_node(flds, 0, 0);

        Output_TreeNode ot = new Output_TreeNode();
        Console.WriteLine("root = \n" + ot.output(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        TreeNode result = ConvertBST(root);
        Console.WriteLine("result = \n" + ot.output(result));

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
