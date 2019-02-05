using System;

//Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution
{
    public ListNode SwapPairs(ListNode head)
    {
        ListNode node = head;
        int temp;
        while (node != null)
        {
            if (node.next == null)
                break;
            temp = node.val;
            node.val = node.next.val;
            node.next.val = temp;
            if (node.next.next == null)
                break;
            node = node.next.next;
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
        if (nums == null)
            return "";

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
        string arg_str = args.Replace("[","").Replace("]","").Trim();
        int[] nums = str_to_int_array(arg_str);
        Console.WriteLine("nums = " + output_int_array(nums));

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums);
        Console.WriteLine("head = " + ope.output_ListNode(head));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result = SwapPairs(head);

        sw.Stop();
        Console.WriteLine("result = " + ope.output_ListNode(result));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
