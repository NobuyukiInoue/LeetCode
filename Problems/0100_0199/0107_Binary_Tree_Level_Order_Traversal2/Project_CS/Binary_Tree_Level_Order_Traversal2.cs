using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    public List<List<int>> LevelOrderBottom(TreeNode root)
    {
        var result = new List<List<int>>();
        if(root == null) return result;
        
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        while(true)
        {
            int nodeCount = queue.Count;
            if(nodeCount == 0)
            {
                break;
            }
            
            var subList = new List<int>();
            while(nodeCount > 0)
            {
                var dataNode = (TreeNode)queue.Dequeue();
                
                subList.Add(dataNode.val);
                
                if(dataNode.left != null)
                {
                    queue.Enqueue(dataNode.left);
                }
                
                if(dataNode.right != null)
                {
                    queue.Enqueue(dataNode.right);
                }
                
                nodeCount--;
            }
            
            result.Insert(0, subList);
        }
        
        return result;
    }

    public string ListListArrayToString(List<List<int>> list)
    {
        if (list == null)
            return "";

        string resultStr = "[\n";
        for (int i = 0; i < list.Count; ++i)
        {
            if (list[i].Count <= 0)
                continue;

            resultStr += "  [" + String.Join(",", list[i]) + "]\n";
        }

        return resultStr + "]\n";
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

        List<List<int>> result = LevelOrderBottom(root);

        sw.Stop();
        Console.WriteLine("result = \n" + ListListArrayToString(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
