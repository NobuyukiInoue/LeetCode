using System;

// Definition for singly-linked list.

public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) {
        val = x;
        next = null;
    }
}

public class Solution {
    public ListNode RemoveElements(ListNode head, int val)
    {
        ListNode dummy = new ListNode(-1);
        ListNode curr = dummy;

        while (head != null) {
            if (head.val != val) {
                curr.next = head;
                curr = curr.next;
                head = head.next;
            }
            else
                head = head.next;
        }

        curr.next = null;
        return dummy.next;
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
        string[] flds = args.Replace(" ", "").Replace("[[", "").Replace("]]", "").Split("],[", StringSplitOptions.None);
        int[] nums = str_to_int_array(flds[0]);
        int k = int.Parse(flds[1]);

        Operate_ListNode ope = new Operate_ListNode();
        ListNode node = ope.set_ListNode(nums);
        Console.WriteLine("node = " + ope.output_ListNode(node));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_node = RemoveElements(node, k);
        sw.Stop();

        Console.WriteLine("Result = " + ope.output_ListNode(result_node));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
