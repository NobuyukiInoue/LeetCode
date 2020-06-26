public class Solution {
    public ListNode middleNode(ListNode head) {
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        ListNode result = middleNode(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
