public class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        // 0ms
        ListNode newHead = head;
        ListNode a = newHead;
        ListNode b = newHead;
        while (n > 0) {
            b = b.next;
            n--;
        }
        if (b == null)
            return head.next;
        while (b.next != null) {
            b = b.next;
            a = a.next;
        }
        a.next = a.next.next;
        return newHead;
    }

    public ListNode removeNthFromEnd2(ListNode head, int n) {
        // 0ms
        ListNode newHead = new ListNode(0);
        newHead.next = head;
        ListNode a = newHead;
        ListNode b = newHead;
        while (n > 0) {
            b = b.next;
            n--;
        }
        while (b.next != null) {
            b = b.next;
            a = a.next;
        }
        a.next = a.next.next;
        return newHead.next;
    }

    /* Solution3
    // 0ms
    class Res {
        int depth_max;
        ListNode node;
        Res(int m, ListNode n) {
            depth_max = m;
            node = n;
        }
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (n <= 0)
            return head;

        if (head == null)
            return null;

        Res res = get_depth(head, 0, n);
        return res.node;
    }

    private Res get_depth(ListNode node, int current_depth, int n) {
        if (node == null) {
            return (new Res(current_depth, node));
        } else {
            Res res = get_depth(node.next, current_depth + 1, n);
            node.next = res.node;
            if (current_depth == res.depth_max - n) {
                if (n == 1) {
                    node = null;
                } else {
                    node = node.next;
                }
            }
            return (new Res(res.depth_max, node));
        }
    }
    */

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateListNode ope = new OperateListNode();
        ListNode head = ope.createListNode(flds[0]);
        int n = Integer.parseInt(flds[1]);
        System.out.println("head = " + ope.listNodeToString(head));
        System.out.println("n = " + n);

        long start = System.currentTimeMillis();

        ListNode result = removeNthFromEnd(head, n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
