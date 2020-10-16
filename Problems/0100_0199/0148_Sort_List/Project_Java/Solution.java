public class Solution {
    public ListNode sortList(ListNode head) {
        // 3ms
        if (head == null || head.next == null)
            return head;

        ListNode prev = null, slow = head, fast = head;

        while (fast != null && fast.next != null) {
            prev = slow;
            slow = slow.next;
            fast = fast.next.next;
        }

        prev.next = null;
        ListNode h1 = sortList(head);
        ListNode h2 = sortList(slow);

        return merge(h1, h2);
    }

    ListNode merge(ListNode h1, ListNode h2) {
        ListNode dummy = new ListNode(0), tail = dummy;

        while (h1 != null && h2 != null) {
            if (h1.val < h2.val) {
                tail.next = h1;
                h1 = h1.next;
            } else {
                tail.next = h2;
                h2 = h2.next;
            }
            tail = tail.next;
        }

        if (h1 != null)
            tail.next = h1;
        if (h2 != null)
            tail.next = h2;
        return dummy.next;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        ListNode result = sortList(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
