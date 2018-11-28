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

    public ListNode set_Nodes(int[] data)
    {
        if (data.Length <= 0) {
            return null;
        }

        ListNode result_nodes = new ListNode(data[0]);
        ListNode next_nodes = result_nodes;

        for (int i = 1; i < data.Length; ++i) {
            next_nodes.next = new ListNode(data[i]);
            next_nodes = next_nodes.next;
        }

        return result_nodes;
    }

    public void output_Nodes(ListNode data)
    {
        ListNode next_nodes = data;

        while (next_nodes != null) {
            Console.Write(next_nodes.val);
            next_nodes = next_nodes.next;
            if (next_nodes != null) {
                Console.Write("->");
            }
        }
        Console.WriteLine();
    }

    public int[] array_string_to_int(string[] words)
    {
        int[] data = new int[words.Length];

        for (int i = 0; i < words.Length; ++i) {
            data[i] = int.Parse(words[i]);
        }

        return data;
    }

    public void Main(string args)
    {
        Console.WriteLine("array = " + args );

        string[] target_str = args.Split(',');
        int[] target_data = array_string_to_int(target_str);
        ListNode target_nodes = set_Nodes(target_data);
        output_Nodes(target_nodes);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_nodes = DeleteDuplicates(target_nodes);
        output_Nodes(result_nodes);
        
        sw.Stop();

        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
