public class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        // 0ms
        if (head == null)
            return null;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;

        for (int i = 0; i < m - 1; i++)
            pre = pre.next;
        
        ListNode start = pre.next;
        ListNode then = start.next;
        
        for (int i = 0; i < n - m; i++) {
            start.next = then.next;
            then.next = pre.next;
            pre.next = then;
            then = start.next;
        }
        return dummy.next;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] nums0 = mc.str_to_int_array(flds[0]);
        Operate_ListNode ope = new Operate_ListNode();
        ListNode head = ope.set_ListNode(nums0);
        System.out.println("head = " + ope.output_ListNode(head));

        String[] nums1 = flds[1].split(",");
        int m = Integer.parseInt(nums1[0]);
        int n = Integer.parseInt(nums1[1]);
        System.out.println("m = " + Integer.toString(m) + ", n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        ListNode result = reverseBetween(head, m, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.output_ListNode(result));
        System.out.println((end - start)  + "ms\n");
    }
}
