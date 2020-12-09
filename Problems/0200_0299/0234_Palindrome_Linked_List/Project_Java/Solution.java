public class Solution {
    public boolean isPalindrome(ListNode head) {
        // 0ms
        if (head == null) {
            return true;
        }

        ListNode p1 = head;
        ListNode p2 = head;
        ListNode p3 = p1.next;
        ListNode pre = p1;

        //find mid pointer, and reverse head half part
        while (p2.next != null && p2.next.next != null) {
            p2 = p2.next.next;
            pre = p1;
            p1 = p3;
            p3 = p3.next;
            p1.next = pre;
        }

        //odd number of elements, need left move p1 one step
        if (p2.next == null) {
            p1 = p1.next;
        }

        //compare from mid to head/tail
        while (p3 != null) {
            if (p1.val != p3.val) {
                return false;
            }
            p1 = p1.next;
            p3 = p3.next;
        }

        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds);
        System.out.println("head = " + ope.listNodeToString(head));

        long start = System.currentTimeMillis();

        boolean result = isPalindrome(head);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
