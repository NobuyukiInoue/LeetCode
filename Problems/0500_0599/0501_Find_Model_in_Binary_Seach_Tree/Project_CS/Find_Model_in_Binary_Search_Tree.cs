using System;

public class Solution {
    public int[] FindMode(TreeNode root)
    {
        int[] nums = new int[1];

        return nums;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.CreateTreeNode(flds);
        Console.Write("node = \n" + ope_t.TreeToStaircaseString(root));
        Console.WriteLine("node = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int[] result = FindMode(root);

        sw.Stop();
        Mylib ml = new Mylib();
        Console.WriteLine("result = " + ml.IntArrayToString(result) );
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
