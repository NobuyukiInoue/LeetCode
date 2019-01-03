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
    public int PathSum(TreeNode root, int sum)
    {
        
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
        
        TreeNode node = new TreeNode(int.Parse(flds[cur_pos + pos]));
        node.left = set_node(flds, depth + 1, 2*pos);
        node.right = set_node(flds, depth + 1, 2*pos + 1);

        return node;
    }

    List<string> resultStr = new List<string>();
    public void output_tree(tree node, int n)
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

    public void print_result()
    {
        for (int i = 0; i < resultStr.Count; ++i)
        {
            Console.WriteLine(resultStr[i]);
        }
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Split(new string[] {"],"}, StringSplitOptions.None);
        string[] root_str = flds[0].Replace("root = ", "").Replace("[", "").Split(',');
        TreeNode node = set_node(arg1);
        string sum = int.Parse(flds[1].Replace("sum = ", ""));

        Console.WriteLine("node = " + output_node(node));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("result = " + PathSum(node, sum) );

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
