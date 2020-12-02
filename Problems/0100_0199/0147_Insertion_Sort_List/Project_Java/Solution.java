public class Solution {
    public ListNode insertionSortList(ListNode head) {
        // 2ms
        ListNode p = new ListNode(0);
        ListNode cur = head;
        ListNode dummy = p;
        dummy.next = head;

        while (cur != null && cur.next != null) {
            int val = cur.next.val;
            if (cur.val < val) {
                cur = cur.next;
                continue;
            }

            if (p.next.val > val)
                p = dummy;

            while (p.next.val < val)
                p = p.next;

            ListNode temp = cur.next;
            cur.next = temp.next;
            temp.next = p.next;
            p.next = temp;
        }

        return dummy.next;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        ListNode result = insertionSortList(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
