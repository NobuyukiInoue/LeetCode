using System;

// * Definition for singly-linked list.
 public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) {
        val = x;
    }
}
 
public class Solution {
    public ListNode DeleteDuplicates(ListNode head) {
        // 114ms - 131ms
        if (head == null || head.next == null) {
            return head;
        }
        ListNode node = head;
        while (node != null && node.next != null) {
            if (node.val == node.next.val) {
                node.next = node.next.next;
            } else {
                node = node.next;
            }
        }
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
        string flds = args.Replace("[", "").Replace("]", "").Trim();

        int[] nums = str_to_int_array(flds);
        Console.WriteLine("nums = " + output_int_array(nums));

    	Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums);
        Console.WriteLine("head = " + ope.output_ListNode(head));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_nodes = DeleteDuplicates(head);

        sw.Stop();

        Console.WriteLine("result = " + ope.output_ListNode(result_nodes));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
