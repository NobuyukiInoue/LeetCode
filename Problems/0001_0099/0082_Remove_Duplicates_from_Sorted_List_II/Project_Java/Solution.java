public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        // 0ms
        if (head == null || head.next == null)
            return head;

        ListNode curr = head;
        ListNode prev = new ListNode(Integer.MIN_VALUE);
        prev.next = head;
        ListNode last = prev;
        ListNode next = head.next;

        while (next != null) {
            if (next.val != curr.val) {
                last = curr;
            } else {
                while (next != null && curr.val == next.val) {
                    next = next.next;
                }
                last.next = next;
                if (next == null) {
                    break;
                }
            }
            curr = next;
            next = next.next;
        }

        return prev.next;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        ListNode result = deleteDuplicates(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
