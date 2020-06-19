using System;

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

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode t1 = ope_t.CreateTreeNode(flds[0]);
        TreeNode t2 = ope_t.CreateTreeNode(flds[1]);

        Console.Write("t1 = \n" + ope_t.TreeToStaircaseString(t1));
        Console.WriteLine("t1 = " + ope_t.Tree2str(t1));
        Console.Write("t2 = \n" + ope_t.TreeToStaircaseString(t2));
        Console.WriteLine("t2 = " + ope_t.Tree2str(t2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        TreeNode result = MergeTrees(t1, t2);

        sw.Stop();
        Console.Write("result = \n" + ope_t.TreeToStaircaseString(result));
        Console.WriteLine("result = " + ope_t.Tree2str(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
