public class Solution {
    public ListNode swapPairs(ListNode head) {
        // 0ms
        ListNode node = head;
        while (node != null) {
            if (node.next == null) {
                break;
            }
            int temp = node.val;
            node.val = node.next.val;
            node.next.val = temp;
            node = node.next.next;
        }
        return head;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = [" + ope.listNodeToString(head) + "]");

        long start = System.currentTimeMillis();

        ListNode result = swapPairs(head);

        long end = System.currentTimeMillis();

        System.out.println("result = [" + ope.listNodeToString(result) + "]");
        System.out.println((end - start)  + "ms\n");
    }
}
