using System;

// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class myClass
{
    static public void Main()
    {
        int[] data1 = { 1, 2, 4};
        int[] data2 = { 1, 3, 4};

        ListNode l1 = set_ListNode(data1);
        ListNode l2 = set_ListNode(data2);

        Solution sl = new Solution(); 
        ListNode l3 = sl.MergeTwoLists(l1, l2);
        ListNode temp_node = l3;

        do {
            Console.Write((temp_node.val).ToString() + " ");
            temp_node = temp_node.next;
        } while (temp_node != null);
    }

    static ListNode set_ListNode(int[] data)
    {
        ListNode l1 = new ListNode(data[0]);
        ListNode temp_node = l1;

        for (int i = 1; i < data.Length; i++) {
            temp_node.next = new ListNode(data[i]);
            temp_node = temp_node.next;
        }

        return l1;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
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
}

