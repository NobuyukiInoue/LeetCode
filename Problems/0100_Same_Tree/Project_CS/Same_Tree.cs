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
        TreeNode p = ope_t.set_TreeNode(nums1);
        TreeNode q = ope_t.set_TreeNode(nums2);

        Console.Write("p = \n" + ope_t.output_TreeNode(p));
        Console.Write("q = \n" + ope_t.output_TreeNode(q));
        Console.WriteLine("p = " + ope_t.Tree2str(p));
        Console.WriteLine("q = " + ope_t.Tree2str(q));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("result = " + IsSameTree(p, q).ToString() );

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
