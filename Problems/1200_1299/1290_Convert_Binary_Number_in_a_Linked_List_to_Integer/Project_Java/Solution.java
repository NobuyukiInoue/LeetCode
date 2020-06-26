public class Solution {
    public int getDecimalValue(ListNode head) {
        // 0ms
        int total = 0;
        while (head != null) {
            total <<= 1;
            total += head.val;
            head = head.next;
        }
        return total;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        int result = getDecimalValue(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
