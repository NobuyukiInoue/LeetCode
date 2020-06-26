public class Solution {
    public ListNode oddEvenList(ListNode head) {
        // 0ms
        if (head == null || head.next == null)
            return head;

        ListNode next_head = head.next;
        ListNode cursor = head;
        int count = 1;
        ListNode last_odd_node = null;

        while (cursor != null) {
            if (count % 2 == 1)
                last_odd_node = cursor;
            ListNode temp_next = cursor.next;
            if (cursor.next != null)
                cursor.next = cursor.next.next;
            cursor = temp_next;
            count++;
        }

        last_odd_node.next = next_head;

        return head;       
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        ListNode result = oddEvenList(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
