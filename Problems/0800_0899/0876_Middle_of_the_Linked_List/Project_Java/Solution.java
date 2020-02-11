public class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] nums = mc.stringTointArray(flds);

        System.out.println("nums = " + mc.intArrayToString(nums));

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums);
        System.out.println("head = " + ope.output_ListNode(head));

        long start = System.currentTimeMillis();

        ListNode result = middleNode(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
