using System;

// Definition for a binary tree node.
public class TreeNode
{
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

public class Solution
{
    public TreeNode MergeTrees(TreeNode t1, TreeNode t2)
    {
        if (t1 == null &&  t2 == null)
        {
            return null;
        }
        else if (t1 != null && t2 != null)
        {
            TreeNode node = new TreeNode(t1.val + t2.val);
            node.left = MergeTrees(t1.left, t2.left);
            node.right = MergeTrees(t1.right, t2.right);
            return node;
        }
        else if (t1 != null)
        {
            TreeNode node = new TreeNode(t1.val);
            node.left = MergeTrees(t1.left, null);
            node.right = MergeTrees(t1.right, null);
            return node;
        }
        else if (t2 != null)
        {
            TreeNode node = new TreeNode(t2.val);
            node.left = MergeTrees(null, t2.left);
            node.right = MergeTrees(null, t2.right);
            return node;
        }
        else
        {
            return null;
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
        TreeNode t1 = ope_t.set_node(nums1, 0, 0);
        TreeNode t2 = ope_t.set_node(nums2, 0, 0);

        Console.WriteLine("t1 = \n" + ope_t.output(t1));
        Console.WriteLine("t2 = \n" + ope_t.output(t2));
        Console.WriteLine("t1 = " + ope_t.Tree2str(t1));
        Console.WriteLine("t2 = " + ope_t.Tree2str(t2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();

        sw.Start();
        TreeNode result = MergeTrees(t1, t2);
        sw.Stop();

        Console.WriteLine("result = \n" + ope_t.output(result));
        Console.WriteLine("result = " + ope_t.Tree2str(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
