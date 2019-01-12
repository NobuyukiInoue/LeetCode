using System;
using System.Collections.Generic;

/* Definition for a binary tree node. */
 public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}
 
public class Solution
{
    public int GetMinimumDifference(TreeNode root)
    {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        TreeNode curr = root;
        int diff = int.MaxValue;
        int prev = 0;
        bool first = true;
        while (curr != null || stack.Count > 0)
        {
            if (curr != null)
            {
                stack.Push(curr);
                curr = curr.left;
            }
            else
            {
                curr = stack.Pop();
                if (!first) diff = Math.Min(diff, Math.Abs(prev - curr.val));
                else first = false;
                prev = curr.val;
                
                curr = curr.right;
            }
        }
        return diff;
    }
    public IList<int> vals;
    public int GetMinimumDifference2(TreeNode root)
    {
        vals = new List<int>();
        get_all_vals2(root);
        int diff_min = int.MaxValue;
        for (int i = 0; i < vals.Count; ++i)
        {
            for (int j = i + 1; j < vals.Count; ++j)
            {
                int temp = Math.Abs(vals[i] - vals[j]);
                if (temp < diff_min)
                    diff_min = temp;
            }
        }
        vals = null;
        return diff_min;
    }

    private void get_all_vals2(TreeNode node)
    {
        if (node == null)
            return;
        vals.Add(node.val);
        if (node.left != null)
            get_all_vals2(node.left);
        if (node.right != null)
            get_all_vals2(node.right);
        return;
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

        string resultStr = "[" +  nums[0].ToString();
 
        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }

        return resultStr + "]";
    }


    public void Main(string args)
    {
        string flds = args.Replace("[[","").Replace("]]","").Trim();
        TreeNode root = set_node(flds.Split(','), 0, 0);
        Output_TreeNode ot = new Output_TreeNode();

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = GetMinimumDifference(root);
        Console.WriteLine("result = " + result.ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}

public class Output_TreeNode
{
    List<string> resultStr = new List<string>();
    public string output(TreeNode node)
    {
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

        return outputStr;
    }
}
