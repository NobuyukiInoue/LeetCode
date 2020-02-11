public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode curr = head;
        int count = 0;
        while (curr != null && count != k) {
            curr = curr.next;
            count++;
        }
        if (count == k) {
            curr = reverseKGroup(curr, k);
            while (count-- > 0) {
                ListNode tmp = head.next;
                head.next = curr;
                curr = head;
                head = tmp;
            }
            head = curr;
        }
        return head;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums1 = mc.stringTointArray(flds[0]);
        int k = Integer.parseInt(flds[1]);

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums1);
        System.out.println("head = " + ope.output_ListNode(head) + ", k = " + Integer.toString(k) );

        long start = System.currentTimeMillis();

        ListNode result = reverseKGroup(head, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
