using System;

/* Definition for singly-linked list. */
public class ListNode
{
     public int val;
     public ListNode next;
     public ListNode(int x) { val = x; }
}

public class Solution {
    public ListNode GetIntersectionNode(ListNode headA, ListNode headB)
    {
        if (headA == null || headB == null)
            return null;
        var nodeA = headA;
        var nodeB = headB;
        
        while (nodeA != null || nodeB != null){
            //if (nodeA == nodeB)
            if (isSameNode(nodeA, nodeB))
                return nodeA;
            nodeA = nodeA != null ? nodeA.next : headB;
            nodeB = nodeB != null ? nodeB.next : headA;
        }
        return null;
    }

    public bool isSameNode(ListNode nodeA, ListNode nodeB)
    {
        if (nodeA == null && nodeB == null)
            return true;
        if (nodeA != null && nodeB != null)
        {
            if (nodeA.val == nodeB.val)
                return isSameNode(nodeA.next, nodeB.next);
            else
                return false;
        }
        return false;
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
        Console.WriteLine("args = " + args );
        string[] flds = args.Replace("\"", "").Replace("[[", "").Replace("]]", "").Trim().Split("],[", StringSplitOptions.None);
        int[] nums1 = str_to_int_array(flds[0]);
        int[] nums2 = str_to_int_array(flds[1]);

        Operate_ListNode ope = new Operate_ListNode();
        ListNode node1 = ope.set_nodes(nums1);
        ListNode node2 = ope.set_nodes(nums2);

        Console.WriteLine("node1 = " + ope.output_nodes(node1));
        Console.WriteLine("node2 = " + ope.output_nodes(node2));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        ListNode result_node = GetIntersectionNode(node1, node2);
        Console.WriteLine("Result = " + ope.output_nodes(result_node));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
