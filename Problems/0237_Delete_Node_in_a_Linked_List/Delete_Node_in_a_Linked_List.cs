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

    private ListNode set_node(string[] flds)
    {
        if (flds.Length == 0)
            return null;

        ListNode node = new ListNode(int.Parse(flds[0]));

        ListNode work_node = node;
        for (int i = 1; i < flds.Length; ++i)
        {
            work_node.next = new ListNode(int.Parse(flds[i]));
            work_node = work_node.next;
        }

        return node;
    }

    public string output_ListNode(ListNode node)
    {
        if (node == null)
            return "";

        string resultStr = node.val.ToString();
        ListNode work_node = node.next;
        while (work_node != null)
        {
            resultStr += " -> " + work_node.val.ToString();
            work_node = work_node.next;
        }

        return resultStr;
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

    public void Main(string args)
    {
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);
        string[] nums1 = flds[0].Split(',');
        string[] nums2 = flds[1].Split(',');

        ListNode node = set_node(nums1);

        Console.WriteLine("node = " + output_ListNode(node));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        DeleteNode(node);
        Console.WriteLine("node = " + output_ListNode(node));

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
