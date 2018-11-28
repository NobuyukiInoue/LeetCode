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
    
    private ListNode set_node(string[] data)
    {
        ListNode node, temp_node;
        
        if (data.Length <= 0)
            return null;

        if (data[0] == "")
            return null;

        node = new ListNode(int.Parse(data[0]));
        temp_node = node;

        for (int i = 1; i < data.Length; i++) {
            temp_node.next = new ListNode(int.Parse(data[i]));
            temp_node = temp_node.next;
        }
        
        return node;
    }
    
    private string output_node(ListNode node)
    {
        if (node == null)
            return "";

        ListNode temp_node = node;
        string resultStr = "";

        if (node == null) {
            return resultStr;
        }
        
        resultStr += temp_node.val.ToString();
        temp_node = temp_node.next;

        while (temp_node != null) {
            resultStr += "," + temp_node.val.ToString();
            temp_node = temp_node.next;
        }
        
        return resultStr;
    }

    public void Main(string args)
    {
        string[] flds = args.Split(new string[] {", "}, StringSplitOptions.None);
        string[] data = flds[0].Replace("[","").Replace("]","").Split(',');
        int k = int.Parse(flds[1]);

        ListNode node = set_node(data);
        Console.WriteLine("node = " + output_node(node));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_node = RemoveElements(node, k);
        Console.WriteLine("Result = " + output_node(result_node));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
