public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;

        while (p != null || q != null)
        {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null)
                p = p.next;
            if (q != null)
                q = q.next;
        }

        if (carry > 0)
        {
            curr.next = new ListNode(carry);
        }

        return dummyHead.next;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateListNode ope = new OperateListNode();
        ListNode l1 = ope.createListNode(flds[0]);
        ListNode l2 = ope.createListNode(flds[1]);
        System.out.println("l1 = " + ope.listNodeToString(l1));
        System.out.println("l2 = " + ope.listNodeToString(l2));

        long start = System.currentTimeMillis();

        ListNode result = AddTwoNumbers(l1, l2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
