public class Solution {
    public ListNode insertGreatestCommonDivisors(ListNode head) {
        // 2ms
        ListNode node = head;
        while (node.next != null) {
            ListNode temp = node.next;
            node.next = new ListNode(gcd(node.val, node.next.val));
            node.next.next = temp;
            node = node.next.next;
        }        
        return head;
    }

    public int gcd(int num1, int num2) {
        if (num2 == 0) {
           return num1;
        } else {
            return gcd(num2, num1%num2);
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        ListNode result = insertGreatestCommonDivisors(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
