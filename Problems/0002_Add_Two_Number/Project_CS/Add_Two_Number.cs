using System;

//Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution
{
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;

        while (p != null || q != null)
        {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null)
                p = p.next;
            if (q != null)
                q = q.next;
        }

        if (carry > 0)
        {
            curr.next = new ListNode(carry);
        }

        return dummyHead.next;        
    }

    public int[] str_to_int_array(string s)
    {
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

    public ListNode set_nodes(int[] nums, int index)
    {
        if (index >= nums.Length)
            return null;
        
        ListNode node = new ListNode(nums[index]);
        node.next = set_nodes(nums, index + 1);

        return node;
    }

    public string output_nodes(ListNode ll)
    {
        string retStr = ll.val.ToString(); 

        if (ll.next != null)
            retStr += " -> " + output_nodes(ll.next);

        return (retStr);
    }

    public void Main(string args)
    {
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] num1 = str_to_int_array(flds[0]);
        int[] num2 = str_to_int_array(flds[1]);
        Console.WriteLine("num1 = " + output_int_array(num1));
        Console.WriteLine("num2 = " + output_int_array(num2));

        ListNode l1 = set_nodes(num1, 0);
        ListNode l2 = set_nodes(num2, 0);
        Console.WriteLine("l1 = " + output_nodes(l1));
        Console.WriteLine("l2 = " + output_nodes(l2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result = AddTwoNumbers(l1, l2);
        Console.WriteLine("result = " + output_nodes(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
