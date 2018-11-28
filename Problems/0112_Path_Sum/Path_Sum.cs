using System;

// Definition for a binary tree node.
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) {
        val = x;
    }
}

public class Solution {
    public bool HasPathSum(TreeNode root, int sum)
    {
        if (root == null) {
            Console.WriteLine("root.val = null, " + "sum =  " + sum.ToString());
        }
        else {
            Console.WriteLine("root.val = " + root.val.ToString() + ", sum = " + sum.ToString());
        }

        if (root == null) {
            return false;
        }

        if ((root.left == null) && (root.right == null)) {
            if (root.val == sum) {
                Console.WriteLine("root.val = " + root.val.ToString() + ", root.left = null, root.right = null, sum= " + sum.ToString() + ", return(true)");
                return true;
            }
            else {
                Console.WriteLine("root.val = " + root.val.ToString() + ", root.left = null, root.right = null, sum= " + sum.ToString() + ", return(false)");
                return false;
            }
        }
        if (root.left != null) {
            if (HasPathSum(root.left, sum - root.val)) {
                return true;
            }
        }
        if (root.right != null) {
            if (HasPathSum(root.right, sum - root.val)) {
                return true;
            }
        }

        return false;
    }

    private void load_treeData(TreeNode root, string data)
    {
        if (data.Length == 0)
            Console.WriteLine("load_treeData() ... arg data Error");
        
        string[] args = data.Split(',');
        if (args[0] != "null") {

        }

        root.val = data[0];
    }

    private TreeNode load_sample0_treeData()
    {
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(4);
        root.right = new TreeNode(8);
        root.left.left = new TreeNode(11);
        root.left.left.left = new TreeNode(7);
        root.left.left.right = new TreeNode(2);
        root.right.left = new TreeNode(13);
        root.right.right = new TreeNode(4);
        root.right.right.right = new TreeNode(1);

        return root;
    }

    private TreeNode load_sample2_treeData()
    {
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);

        return root;
    }

    public void Main(string args)
    {
    //    Console.WriteLine("args = " + args);    
    //    string s = args.Replace("\"", "");

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

    //    TreeNode root = load_sample0_treeData();
    //    Console.WriteLine("Result = " + HasPathSum(root, 22).ToString());

        TreeNode root = load_sample2_treeData();
        Console.WriteLine("Result = " + HasPathSum(root, 1).ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
