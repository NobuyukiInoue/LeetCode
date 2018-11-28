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

    private TreeNode set_node(string[] data)
    {
        if (data.Length == 0) {
            return null;
        }

        TreeNode new_node = new TreeNode(int.Parse(data[0]));
        if (data[1] != "null") {
            new_node.left = new TreeNode(int.Parse(data[1]));
        }
        if (data[2] != "null") {
            new_node.right = new TreeNode(int.Parse(data[2]));
        }

        return new_node;
    }

    private string output_node(TreeNode node)
    {
        string tempStr = "";

        if (node != null) {
            tempStr += node.val + ",";
        }
        if (node.left != null) {
            tempStr += node.left.val + ",";
        }
        else {
            tempStr += "null,";
        }
        if (node.right != null) {
            tempStr += node.right.val;
        }
        else
        {
            tempStr += "null";
        }

        return tempStr;
    }
    public void Main(string args)
    {
        Console.WriteLine("args = " + args );

    //    string[] workStr = args.Split('\t');
        string[] workStr = args.Split((char)0x09);    // [TAB]

        string[] arg1 = workStr[0].Split(',');
        string[] arg2 = workStr[1].Split(',');

        TreeNode p = set_node(arg1);
        TreeNode q = set_node(arg2);

        Console.WriteLine("p = " + output_node(p));
        Console.WriteLine("q = " + output_node(q));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("result = " + IsSameTree(p, q).ToString() );

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
