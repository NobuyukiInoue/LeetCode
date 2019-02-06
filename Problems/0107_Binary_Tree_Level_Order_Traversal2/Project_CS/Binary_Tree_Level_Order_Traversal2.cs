using System;
using System.Collections.Generic;
using System.Linq;

// Definition for a binary tree node.
 public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

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

    public string output_int_array(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = nums[0].ToString();

        for (int i = 1; i < resultStr.Length; ++i)
        {
            resultStr += ", " + nums[i].ToString();
        }

        return resultStr;
    }

    public string output_ListList_Array(List<List<int>> list)
    {
        if (list == null)
            return "";

        string resultStr = "[\n";
        for (int i = 0; i < list.Count; ++i)
        {
            if (list[i].Count <= 0)
                continue;

            resultStr += "\t[" + list[i][0].ToString();
            for (int j = 0; j < list[i].Count; ++j)
            {
                resultStr += ", " + list[i][j].ToString();
            }
            resultStr += "]\n";
        }

        return resultStr + "]\n";
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string flds = args.Replace("\"", "").Replace("[", "").Replace("]", "").Trim();
        string[] nums = flds.Split(',');

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(nums);

        Console.Write("root = \n" + ope_t.output_TreeNode(root));
        Console.WriteLine("root = " + ope_t.Tree2str(root));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        List<List<int>> result = LevelOrderBottom(root);

        sw.Stop();
        Console.WriteLine("result = \n" + output_ListList_Array(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
