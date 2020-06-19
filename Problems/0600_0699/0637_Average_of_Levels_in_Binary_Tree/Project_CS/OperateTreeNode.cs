using System;
using System.Collections.Generic;

public class OperateTreeNode
{
    public TreeNode CreateTreeNode(string flds)
    {
         return CreateSubTreeNode(flds.Split(","), 0, 0);
    }

    private TreeNode CreateSubTreeNode(string[] flds, int depth, int pos)
    {
        if (flds.Length == 0)
            return null;

        int cur_pos = 0;
        for (int i = 0; i < depth; ++i)
            cur_pos += (int)Math.Pow(2, i);
        
        if (cur_pos + pos > flds.Length - 1)
            return null;
        
        if (flds[cur_pos + pos] == "null")
            return null;

        if (flds[cur_pos + pos] == "")
            return null;

        try
        {
            TreeNode node = new TreeNode(int.Parse(flds[cur_pos + pos]));
            node.left = CreateSubTreeNode(flds, depth + 1, 2*pos);
            node.right = CreateSubTreeNode(flds, depth + 1, 2*pos + 1);

            return node;
        }
        catch (Exception e)
        {
            Console.WriteLine("\n" +  e.Message + "\n" +
                              "CreateSubTreeNode() Error ... flds[" + (cur_pos + pos).ToString() + "] = " + flds[cur_pos + pos] + "\n");
            Environment.Exit(-1);

            return null;
        }
    }

    List<string> resultList;

    public string TreeToStaircaseString(TreeNode node)
    {
        resultList = new List<string>();

        string outStr = TreeToStaircaseSubString(node, 0);
        resultList.Clear();

        return outStr;
    }

    private string TreeToStaircaseSubString(TreeNode node, int n)
    {
        if (node == null)
            return "";
        
        if (resultList.Count <= n)
            resultList.Add("(" + node.val.ToString() + ")");
        else
            resultList[n] += ",(" + node.val.ToString() + ")";

        if (node.left != null)
            TreeToStaircaseSubString(node.left, n + 1);
        if (node.right != null)
            TreeToStaircaseSubString(node.right, n + 1);

        return String.Join("\n", resultList) + "\n";
    }

    public string Tree2str(TreeNode node)
    {
        if (node == null)
            return "";

        string resultStr = node.val.ToString();

        if (node.left == null && node.right == null)
            return resultStr;

        resultStr += "(" + Tree2str(node.left) + ")";
        if (node.right != null)
            resultStr += "(" + Tree2str(node.right) + ")";

        return resultStr;
    }
}
