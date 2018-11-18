// Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution {

    static public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        ListNode temp3 = new ListNode(0);

        ListNode_Add(temp1, temp2, temp3);
        
        return temp3;
    }

    static public void ListNode_Add(ListNode l1, ListNode l2, ListNode l3)
    {
        int val1, val2;

        if (l1 == null)
            val1 = 0;
        else
            val1 = l1.val;

        if (l2 == null)
            val2 = 0;
        else
            val2 = l2.val;

        if (l3 == null)
            l3 = new ListNode(val1 + val2);
        else
            l3.val = val1 + val2 + l3.val;
        
        if (l3.val >= 10) {
            l3.val = l3.val % 10;
            l3.next = new ListNode(1);
        }
        else {
            l3.next = new ListNode(0);
        }

        if (l1.next != null || l2.next != null) {
            if (l1.next == null)
                l1.next = new ListNode(0);
            if (l2.next == null)
                l2.next = new ListNode(0);
        
            l3.next = ListNode_Add(l1.next, l2.next, l3.next);
        }
    }
}

