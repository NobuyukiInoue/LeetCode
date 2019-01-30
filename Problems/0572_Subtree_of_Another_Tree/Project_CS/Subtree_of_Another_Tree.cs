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
    public bool IsSubtree(TreeNode s, TreeNode t)
    {
        if (s.val == t.val)
            if (IsSameTree(s, t))
                return true;
        if (s.left != null)
            if (IsSubtree(s.left, t))
                return true;
        if (s.right != null)
            if (IsSubtree(s.right, t))
                return true;
        return false;
    }

    public bool IsSameTree(TreeNode p, TreeNode q)
    {
        if (p == null && q == null) {
            return true;
        }
        else if (p == null || q == null)
        {
            return false;
        }

        if (p.val == q.val) {
            if (IsSameTree(p.left, q.left)) {
                return IsSameTree(p.right, q.right);
            }
            else {
                return false;
            }
        }
        else {
            return false;
        }
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
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);
        string[] nums1 = flds[0].Split(',');
        string[] nums2 = flds[1].Split(',');

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode s = ope_t.set_TreeNode(nums1);
        TreeNode t = ope_t.set_TreeNode(nums2);
        Console.Write("s = \n" + ope_t.output_TreeNode(s));
        Console.WriteLine("s = " + ope_t.Tree2str(s));
        Console.Write("t = \n" + ope_t.output_TreeNode(t));
        Console.WriteLine("t = " + ope_t.Tree2str(t));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsSubtree(s, t);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
