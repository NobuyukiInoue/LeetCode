using System;
using System.Collections.Generic;

// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution {
    public void DeleteNode(ListNode node)
    {
        ListNode prev_node = node;

        while (node != null)
        {
            if (node.next != null)
            {
                prev_node = node;
                node.val = node.next.val;
                node = node.next;
            }
            else
                break;
        }
        prev_node.next = null;
    }

    public int[] str_to_int_array(string s)
    {
        if (s.Length <= 0)
            return null;

        string[] flds = s.Split(',');
        int[] nums = new int[flds.Length];

        if (flds.Length <= 0)
            return nums;

        for (int i = 0; i < nums.Length; ++i)
        {
            nums[i] = int.Parse(flds[i]);
        }

        return nums;
    }

    public string output_int_array(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = "[" +  nums[0].ToString();
 
        for (int i = 1; i < nums.Length; ++i)
        {
            resultStr += "," + nums[i].ToString();
        }

        return resultStr + "]";
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);
        int[] nums1 = str_to_int_array(flds[0]);
        int[] nums2 = str_to_int_array(flds[1]);

        Operate_ListNode ope = new Operate_ListNode();
        ListNode node = ope.set_nodes(nums1);

        Console.WriteLine("node = " + ope.output_nodes(node));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        DeleteNode(node);
        Console.WriteLine("node = " + ope.output_nodes(node));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
