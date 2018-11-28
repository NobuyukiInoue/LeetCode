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
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        if(headA == null || headB == null)
            return null;
        var nodeA = headA;
        var nodeB = headB;
        
        while(nodeA != null || nodeB != null){
            if(nodeA == nodeB)
                return nodeA;
            nodeA = nodeA != null ? nodeA.next : headB;
            nodeB = nodeB != null ? nodeB.next : headA;
        }
        return null;
    }

    public ListNode GetIntersectionNode_old(ListNode headA, ListNode headB)
    {
        ListNode tempHeadA = headA;
        ListNode tempHeadB;
        while (tempHeadA != null) {
            tempHeadB = headB;
            while (tempHeadB != null) {
                if (check_equal(tempHeadA, tempHeadB))
                    return tempHeadA;
                tempHeadB = tempHeadB.next;
            }
            tempHeadA = tempHeadA.next;
        }
        return null;
    }

    private bool check_equal(ListNode headA, ListNode headB)
    {
        ListNode tempHeadA = headA;
        ListNode tempHeadB = headB;
        while (tempHeadA.val == tempHeadB.val) {
            if (tempHeadA.next == null && tempHeadB.next == null)
                return true;
            else if (tempHeadA.next == null)
                return false;
            else if (tempHeadB.next == null)
                return false;
            tempHeadA = tempHeadA.next;
            tempHeadB = tempHeadB.next;
        }

        return false;
    }

    public ListNode GetIntersectionNode_bad(ListNode headA, ListNode headB)
    {
        if (headA != null || headB != null)
            return null;
        int reset = 0;
        ListNode runner_a = headA;
        ListNode runner_b = headB;
        while (reset <= 2) {
            if (runner_a != null) {
                runner_a = headB;
                reset += 1;
            }
            if (runner_b != null) {
                runner_b = headA;
                reset += 1;
            }
            if (runner_a == runner_b)
                return runner_a;
            else {
                runner_a = runner_a.next;
                runner_b = runner_b.next;
            }
        }

        return null;
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
            return "null";
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
        string[] temp = args.Split('\t');
        string[] data1 = temp[0].Split(',');
        string[] data2 = temp[1].Split(',');
        ListNode node1 = set_node(data1);
        ListNode node2 = set_node(data2);

        Console.WriteLine("node1 = " + output_node(node1));
        Console.WriteLine("node2 = " + output_node(node2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_node = GetIntersectionNode(node1, node2);
        Console.WriteLine("Result = " + output_node(result_node).ToString());
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
