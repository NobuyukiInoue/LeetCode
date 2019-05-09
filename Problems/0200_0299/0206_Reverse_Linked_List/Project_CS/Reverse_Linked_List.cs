using System;
using System.Collections.Generic;

// Definition for singly-linked list.

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) {
        val = x;
        next = null;
    }
}


public class Solution
{
    public ListNode ReverseList(ListNode head)
    {
        ListNode newH = null, temp1 = null, temp2 = null;

        while(head != null) {
            temp2 = head;
            head = head.next;
            temp1 = newH;
            newH = temp2;
            newH.next = temp1;
        }

        return newH;
    }

    public ListNode ReverseList_1(ListNode head)
    {
        if (head == null)
            return null;
        
        List<int> node_list = new List<int>();
        ListNode temp_node = head;
        node_list.Add(head.val);

        while (temp_node.next != null) {
            temp_node = temp_node.next;
            node_list.Add(temp_node.val);
        }
        
        ListNode result_top = new ListNode(node_list[node_list.Count - 1]);
        temp_node = result_top;

        for (int i = node_list.Count - 2; i >= 0; --i) {
            temp_node.next = new ListNode(node_list[i]);
            temp_node = temp_node.next;
        }

        return result_top;
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
        string flds = args.Replace("[", "").Replace("]", "");
        int[] nums = str_to_int_array(flds);

        Operate_ListNode ope = new Operate_ListNode();
        ListNode node = ope.set_ListNode(nums);
        Console.WriteLine("node = " + ope.output_ListNode(node));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_node = ReverseList(node);
        Console.WriteLine("Result = " + ope.output_ListNode(result_node));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
