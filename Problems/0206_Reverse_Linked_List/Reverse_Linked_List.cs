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

        ListNode result_node = ReverseList(node);
        Console.WriteLine("Result = " + output_node(result_node));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
