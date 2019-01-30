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
        if (head == null) {
            return null;
        }

        ListNode read_next_nodes = head;
        ListNode result_nodes = new ListNode(head.val);
        ListNode temp_node = result_nodes;

        while (read_next_nodes.next != null) {
            while (read_next_nodes.val == read_next_nodes.next.val)
                if (read_next_nodes.next.next != null)
                    read_next_nodes.next = read_next_nodes.next.next;
                else
                    break;

            if (temp_node.val != read_next_nodes.next.val) {
                temp_node.next = new ListNode(read_next_nodes.next.val);
                temp_node = temp_node.next;
            }
            read_next_nodes = read_next_nodes.next;
        }

        return result_nodes;
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
        ListNode head = ope.set_nodes(nums);
        Console.WriteLine("head = " + ope.output_nodes(head));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_nodes = DeleteDuplicates(head);

        sw.Stop();

        Console.WriteLine("result = " + ope.output_nodes(result_nodes));
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
