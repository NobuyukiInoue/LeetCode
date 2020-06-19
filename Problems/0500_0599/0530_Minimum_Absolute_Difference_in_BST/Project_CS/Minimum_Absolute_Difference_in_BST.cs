using System;
using System.Collections.Generic;

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

    public void Main(string args)
    {
        string flds = args.Replace("[[","").Replace("]]","").Trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.CreateTreeNode(flds);
        Console.Write("root = \n" + ope_t.TreeToStaircaseString(root));
        Console.WriteLine("root = \n" + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = GetMinimumDifference(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
