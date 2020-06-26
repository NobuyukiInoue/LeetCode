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

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds[0]);
        System.out.println("head = " + ope.listNodeToString(head));

        int k = Integer.parseInt(flds[1]);
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        ListNode result = rotateRight(head, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
