using System;

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

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode p = ope_t.CreateTreeNode(flds[0]);
        TreeNode q = ope_t.CreateTreeNode(flds[1]);

        Console.Write("p = \n" + ope_t.TreeToStaircaseString(p));
        Console.Write("q = \n" + ope_t.TreeToStaircaseString(q));
        Console.WriteLine("p = " + ope_t.Tree2str(p));
        Console.WriteLine("q = " + ope_t.Tree2str(q));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        bool result = IsSameTree(p, q);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
