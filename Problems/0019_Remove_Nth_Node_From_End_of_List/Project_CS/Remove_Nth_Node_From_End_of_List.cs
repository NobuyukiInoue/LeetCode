using System;
using System.Collections.Generic;

// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution
{
    public ListNode RemoveNthFromEnd(ListNode head, int n)
    {
        int len = 0;
        ListNode p = head;

        while (p != null)
        {
            p = p.next;
            len++;
        }

        if (len == n)
            return head.next;
        
        p = head;
        int i = 0;
        while (i < len - n - 1)
        {
            p = p.next;
            i++;
        }

        p.next = p.next.next;

        return head;
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
        string[] flds = args.Replace("\"", "").Replace(" ", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);
        int[] nums1 = str_to_int_array(flds[0]);
        int n = int.Parse(flds[1]);

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums1);

        Console.WriteLine("node = " + ope.output_ListNode(head));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result = RemoveNthFromEnd(head, n);
        sw.Stop();

        Console.WriteLine("node = " + ope.output_ListNode(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
