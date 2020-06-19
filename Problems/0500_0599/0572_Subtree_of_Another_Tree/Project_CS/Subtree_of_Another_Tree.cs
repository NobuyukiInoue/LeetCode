using System;

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

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode s = ope_t.CreateTreeNode(flds[0]);
        TreeNode t = ope_t.CreateTreeNode(flds[1]);
        Console.Write("s = \n" + ope_t.TreeToStaircaseString(s));
        Console.WriteLine("s = " + ope_t.Tree2str(s));
        Console.Write("t = \n" + ope_t.TreeToStaircaseString(t));
        Console.WriteLine("t = " + ope_t.Tree2str(t));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsSubtree(s, t);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
