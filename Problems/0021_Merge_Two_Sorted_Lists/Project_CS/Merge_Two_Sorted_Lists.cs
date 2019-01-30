using System;

// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        int n1 = node_count(l1);
        int n2 = node_count(l2);
        
        if (n1 + n2 == 0) {
            return null;
        }

        int[] data = new int[n1 + n2];
        
        int i;
        ListNode temp_node;
        
        temp_node = l1;
        for (i = 0; i < n1; i++) {
            data[i] = temp_node.val;
            temp_node = temp_node.next;
        }

        temp_node = l2;
        for (     ; i < n1 + n2; i++) {
            data[i] = temp_node.val;
            temp_node = temp_node.next;
        }
        
        for (int n = 0; n < data.Length - 1; n++) {
            for (int m = n + 1; m < data.Length; m++) {
                if (data[m] < data[n]) {
                    int temp = data[n];
                    data[n] = data[m];
                    data[m] = temp;
                }
            }
        }
        
        ListNode lst = new ListNode(data[0]);
        temp_node = lst;

        for (int n = 1; n < data.Length; n++) {
            temp_node.next = new ListNode(data[n]);
            temp_node = temp_node.next;
        }
        
        return lst;
    }
    
    static private int node_count(ListNode l1)
    {
        if (l1 == null) 
        {
            return 0;
        }
        
        int i = 0;
        ListNode temp_node;
        
        temp_node = l1;
        while (temp_node.next != null) {
            i++;
            temp_node = temp_node.next;
        }
        
        return i + 1;
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
        string arg_str = args.Replace("[[","").Replace("]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"],["}, StringSplitOptions.None);
        int[] num1 = str_to_int_array(flds[0]);
        int[] num2 = str_to_int_array(flds[1]);
        Console.WriteLine("num1 = " + output_int_array(num1));
        Console.WriteLine("num2 = " + output_int_array(num2));

    	Operate_ListNode ope = new Operate_ListNode();
        ListNode l1 = ope.set_nodes(num1);
        ListNode l2 = ope.set_nodes(num2);
        Console.WriteLine("l1 = " + ope.output_nodes(l1));
        Console.WriteLine("l2 = " + ope.output_nodes(l2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result = MergeTwoLists(l1, l2);
        Console.WriteLine("result = " + ope.output_nodes(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
