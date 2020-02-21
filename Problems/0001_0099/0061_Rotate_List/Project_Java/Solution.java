public class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        // 0ms
        if (head == null || head.next == null)
            return head;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode fast = dummy, slow = dummy;
        int i, j;

        for (i = 0; fast.next != null; i++)
            fast = fast.next;
        
        for (j = i - k%i; j > 0; j--)
            slow = slow.next;
        
        fast.next = dummy.next;
        dummy.next = slow.next;
        slow.next = null;
        
        return dummy.next;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringTointArray(flds[0]);

        System.out.println("nums = " + ml.intArrayToString(nums));

        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums);
        System.out.println("head = " + ope.output_ListNode(head));

        int k = Integer.parseInt(flds[1]);
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        ListNode result = rotateRight(head, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
