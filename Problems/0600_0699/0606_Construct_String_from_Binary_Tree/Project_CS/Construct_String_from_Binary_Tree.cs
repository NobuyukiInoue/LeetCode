using System;

public class Solution
{
    public string Tree2str(TreeNode t)
    {
        if (t == null)
            return "";

        string resultStr = t.val.ToString();

        if (t.left == null && t.right == null)
            return resultStr;

        resultStr += "(" + Tree2str(t.left) + ")";
        if (t.right != null)
            resultStr += "(" + Tree2str(t.right) + ")";

        return resultStr;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode t = ope_t.CreateTreeNode(flds);
        Console.Write("t = \n" + ope_t.TreeToStaircaseString(t));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string result = Tree2str(t);

        sw.Stop();
        Console.WriteLine("result = " + result);
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
