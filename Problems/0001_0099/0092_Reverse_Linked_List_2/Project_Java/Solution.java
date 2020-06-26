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

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds[0]);
        System.out.println("head = " + ope.listNodeToString(head));

        String[] nums1 = flds[1].split(",");
        int m = Integer.parseInt(nums1[0]);
        int n = Integer.parseInt(nums1[1]);
        System.out.println("m = " + Integer.toString(m) + ", n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        ListNode result = reverseBetween(head, m, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
