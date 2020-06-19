using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public TreeNode ConvertBST(TreeNode root)
    {
        TreeNode node = root;
        Stack<TreeNode> stack = new Stack<TreeNode>();

        int sum = 0;
        while (node != null || stack.Count > 0)
        {
            if (node != null)
            {
                stack.Push(node);
                node = node.right;
            }
            else
            {
                // visit
                node = stack.Pop();
                sum += node.val;
                node.val = sum;
                
                node = node.left;
            }
        }
        
        return root;
    }
    
    List<int> nums = new List<int>();
    public TreeNode ConvertBST_work(TreeNode root)
    {
        getAllVal(root);

        nums.Sort();
        nums.Reverse();

        TreeNode resultNode = root;
        setGreater(resultNode);

        return resultNode;
    }

    private void getAllVal(TreeNode node)
    {
        if (node == null)
            return;
        nums.Add(node.val);
        if (node.left != null)
            getAllVal(node.left);
        if (node.right != null)
            getAllVal(node.right);
    }

    public void setGreater(TreeNode node)
    {
        if (node == null)
            return;
        node.val += calc_addVal(node.val);
        if (node.left != null)
            setGreater(node.left);
        if (node.right != null)
            setGreater(node.right);
    }

    private int calc_addVal(int currentVal)
    {
        int addVal = 0;
        for (int i = 0; i < nums.Count; ++i)
            if (nums[i] > currentVal)
                addVal += nums[i];
            else
                break;
        
        return addVal;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.CreateTreeNode(flds);
        Console.Write("root = \n" + ope_t.TreeToStaircaseString(root));
        Console.WriteLine("root = \n" + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        TreeNode result = ConvertBST(root);

        sw.Stop();
        Console.Write("result = \n" + ope_t.TreeToStaircaseString(result));
        Console.WriteLine("result = " + ope_t.Tree2str(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
