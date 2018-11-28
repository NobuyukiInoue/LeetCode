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
    public bool HasCycle(ListNode head)
    {
        if (head == null)
            return false;

        ListNode fastPtr = head, slowPtr = head;

        while(fastPtr != null && fastPtr.next != null) {
            fastPtr = fastPtr.next.next;
            slowPtr = slowPtr.next;
            if (fastPtr == slowPtr) {
                return true;
            }
        }

        return false;
    }
    
    private ListNode set_node(string[] data)
    {
        ListNode node, temp_node;
        
        if (data.Length <= 0) {
            return null;
        }

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
        string[] data = args.Split(',');
        ListNode node = set_node(data);
        Console.WriteLine("node = " + output_node(node));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Console.WriteLine("Result = " + HasCycle(node).ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
