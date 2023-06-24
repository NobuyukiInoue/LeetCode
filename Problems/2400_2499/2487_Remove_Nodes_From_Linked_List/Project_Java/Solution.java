public class Solution {
    public ListNode removeNodes2(ListNode head) {
        // 21ms - 22ms
        if (head != null) {
            head.next = removeNodes2(head.next);
            if (head.next != null && head.val < head.next.val) {
                return head.next;
            }
        }
        return head;
    }

    public ListNode removeNodes(ListNode head) {
        // 6ms
        head = reverseList(head);
        int maximum = Integer.MIN_VALUE;
        ListNode current = head;
        ListNode prev = null;
        while (current != null) {
            ListNode tmp_next = current.next;
            if (current.val >= maximum) {
                maximum = current.val;
                if (prev != null) {
                    prev.next = current;
                    current.next = null;
                } else {
                    head.next = null;
                }
                prev = current;
            }
            current = tmp_next;
        }
        return reverseList(head);
    }

    private ListNode reverseList(ListNode head) {
        ListNode current = head;
        ListNode prev = null;
        while (current != null) {
            ListNode old_next = current.next;
            current.next = prev;
            prev = current;
            current = old_next;
        }
        return prev;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        ListNode result = removeNodes(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
