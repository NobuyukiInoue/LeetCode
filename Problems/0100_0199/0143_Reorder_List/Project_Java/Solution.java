public class Solution {
    public void reorderList(ListNode head) {
        // 2ms
        if (head == null || head.next == null)
            return;

        //Find the middle of the list
        ListNode p1 = head;
        ListNode p2 = head;
        while (p2.next != null && p2.next.next != null) { 
            p1 = p1.next;
            p2 = p2.next.next;
        }

        //Reverse the half after middle  1->2->3->4->5->6 to 1->2->3->6->5->4
        ListNode preMiddle = p1;
        ListNode preCurrent = p1.next;
        while (preCurrent.next != null) {
            ListNode current = preCurrent.next;
            preCurrent.next = current.next;
            current.next = preMiddle.next;
            preMiddle.next = current;
        }

        //Start reorder one by one  1->2->3->6->5->4 to 1->6->2->5->3->4
        p1 = head;
        p2 = preMiddle.next;
        while (p1 != preMiddle) {
            preMiddle.next = p2.next;
            p2.next = p1.next;
            p1.next = p2;
            p1 = p2.next;
            p2 = preMiddle.next;
        }
    }

    public void reorderList_bad(ListNode head) {
        ListNode fast, slow, lo, hi;
        fast = slow = lo = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        hi = null;
        while (slow != null) {
            slow.next = hi;
            slow = slow.next;
            hi = slow;
        }

        while (lo != hi && lo.next != hi) {
            lo.next = hi;
            lo = lo.next;
            hi.next = lo.next;
            hi = hi.next;
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        reorderList(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(head));
        System.out.println((end - start)  + "ms\n");
    }
}
