using System;

public class Solution {
    // * Definition for singly-linked list.
    public class ListNode {
        public int val;
        public ListNode next;
        public ListNode(int x) { val = x; }
    }

    public void Main()
    {
    //  long val1 = 342;
        long n1 = inputVal("val1 = ");
        ListNode val1 = setVal(n1);
        Console.WriteLine("(" + getVal(val1) + ")");

    //  ListNode val2 = setVal(465);
        long n2 = inputVal("val2 = ");
        ListNode val2 = setVal(n2);
        Console.WriteLine("(" + getVal(val2) + ")");

        ListNode val3 = AddTwoNumbers(val1, val2);
        Console.WriteLine();
        Console.WriteLine("(" + getVal(val3) + ")");
    }

    public long inputVal(string msg)
    {
        Console.Write(msg);
        return(long.Parse(Console.ReadLine()));
    }
    public ListNode AddTwoNumbers_old(ListNode l1, ListNode l2) {
        long val1 = getNext(l1);
        long val2 = getNext(l2);

        return (setVal(val1 + val2));
    }

    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp1 = l1;
        ListNode temp2 = l2;
        ListNode temp3 = new ListNode(0);

        return(ListNode_Add(temp1, temp2, temp3));
    }

    public ListNode ListNode_Add(ListNode l1, ListNode l2, ListNode l3)
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
        else
            l3.next = new ListNode(0);

        if (l1.next != null || l2.next != null) {
            if (l1.next == null)
                l1.next = new ListNode(0);
            if (l2.next == null)
                l2.next = new ListNode(0);
        
            l3.next = ListNode_Add(l1.next, l2.next, l3.next);
        }

        return(l3);
    }

    private string getVal(ListNode ll)
    {
        string retStr = ll.val.ToString(); 

        if (ll.next != null)
        {
            retStr += " --> ";
            retStr += getVal(ll.next);
        }

        return (retStr);
    }
   
    private long getNext(ListNode ll)
    {
        if (ll.next == null)
        {
            return ll.val;
        }
        else 
        {
            return (ll.val + 10*getNext(ll.next));
        }
    }

    private ListNode setVal(long x)
    {
        ListNode ll = new ListNode((int)(x % 10));

        if ( x >= 10 )
        {
            ll.next = setVal(x / 10);
        }
        
        return(ll);
    }
}
