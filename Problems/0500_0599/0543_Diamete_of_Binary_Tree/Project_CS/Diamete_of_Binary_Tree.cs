using System;
using System.Collections.Generic;

public class Solution
{
    public int DiameterOfBinaryTree(TreeNode root)
    {
        if (root == null)
            return 0;
        int fnode = 0;
        return RecursiveDiameter(root, ref fnode);
    }

    public int RecursiveDiameter(TreeNode node,ref int fnode)
    {
        if (node == null)
        {
            fnode = 0;
            return 0;
        }
        
        if (node.left == null && node.right == null)
        {
            fnode = 0;
            return 0;
        }
       
        int ldist = 0;
        int rdist = 0;
        
        int ldm = RecursiveDiameter(node.left,ref ldist);
        int rdm = RecursiveDiameter(node.right,ref rdist);
                
        fnode = Math.Max(ldist, rdist) + 1;
        int diameter = ldist + rdist;
        if (node.left != null)
        {
            diameter++;
        }
        if (node.right != null)
        {
            diameter++;
        }
        return Math.Max(diameter, Math.Max(ldm, rdm));
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.CreateTreeNode(flds);
        Console.Write("root = \n" + ope_t.TreeToStaircaseString(root));
        Console.WriteLine("root = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        int result = DiameterOfBinaryTree(root);

        sw.Stop();
        Console.WriteLine("result = " + result.ToString());
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
