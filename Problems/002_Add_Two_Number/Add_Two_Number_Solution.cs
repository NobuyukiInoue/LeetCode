using System;

//Definition for singly-linked list.
public class ListNode {
    public int val;
    public ListNode next;
    public ListNode(int x) { val = x; }
}

public class Solution {

    static public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;        
    }

    static public void Main()
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
    static public long inputVal(string msg)
    {
        Console.Write(msg);
        return(long.Parse(Console.ReadLine()));
    }

    static private string getVal(ListNode ll)
    {
        string retStr = ll.val.ToString(); 

        if (ll.next != null)
        {
            retStr += " --> ";
            retStr += getVal(ll.next);
        }

        return (retStr);
    }
   
    static private long getNext(ListNode ll)
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
    static private ListNode setVal(long x)
    {
        ListNode ll = new ListNode((int)(x % 10));

        if ( x >= 10 )
        {
            ll.next = setVal(x / 10);
        }
        
        return(ll);
    }
}
