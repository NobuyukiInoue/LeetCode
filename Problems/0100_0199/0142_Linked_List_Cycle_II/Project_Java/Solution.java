import java.util.*;

public class Solution {
    public ListNode detectCycle(ListNode head) {
        // 0ms
        if (head == null || head.next == null) {
            return null;
        }
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                while (head != fast) {
                    fast = fast.next;
                    head = head.next;
                }
                return head;
            }
        }
        return null;
    }

    public ListNode detectCycle2(ListNode head) {
        // 3ms
        HashSet nodes = new HashSet();
        ListNode current = head;

        while (current != null){
            if (nodes.contains(current))
                return current;
            nodes.add(current);
            current = current.next;
        }

        return null;
     }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums = mc.stringTointArray(flds[0]);

        System.out.println("nums = " + mc.intArrayToString(nums));

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums);
        System.out.println("head = " + ope.output_ListNode(head));
        int pos = Integer.parseInt(flds[1]);
        System.out.println("pos = " + Integer.toString(pos));

        long start = System.currentTimeMillis();

        ListNode result = detectCycle(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
