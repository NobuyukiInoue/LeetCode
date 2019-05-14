using System;
using System.Collections.Generic;

public class Operate_TreeNode
{
    public TreeNode set_TreeNode(string[] flds)
    {
         return set_TreeNode(flds, 0, 0);
    }

    public TreeNode set_TreeNode(string[] flds, int depth, int pos)
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
            node.left = set_TreeNode(flds, depth + 1, 2*pos);
            node.right = set_TreeNode(flds, depth + 1, 2*pos + 1);

            return node;
        }
        catch (Exception e)
        {
            Console.WriteLine("\n" +  e.Message + "\n" +
                              "set_TreeNode() Error ... flds[" + (cur_pos + pos).ToString() + "] = " + flds[cur_pos + pos] + "\n");
            Environment.Exit(-1);

            return null;
        }
    }

    List<string> resultStr;

    public string output_TreeNode(TreeNode node)
    {
        resultStr = new List<string>();

        string outStr = set_ResultStr(node, 0);
        resultStr.Clear();

        return outStr;
    }

    private string set_ResultStr(TreeNode node, int n)
    {
        if (node == null)
            return "";
        
        if (resultStr.Count <= n)
            resultStr.Add("(" + node.val.ToString() + ")");
        else
            resultStr[n] += ",(" + node.val.ToString() + ")";

        if (node.left != null)
            set_ResultStr(node.left, n + 1);
        if (node.right != null)
            set_ResultStr(node.right, n + 1);

        string outputStr = "";
        for (int i = 0; i < resultStr.Count; ++i)
        {
            outputStr += resultStr[i] + "\n";
        }

        return outputStr;
    }

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
}