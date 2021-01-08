import java.util.*;

public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // 4ms
        Stack<ListNode> s1 = new Stack<>();
        Stack<ListNode> s2 = new Stack<>();
        Stack<ListNode> s3 = new Stack<>();

        while (l1 != null) {
            s1.push(l1);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2);
            l2 = l2.next;
        }

        int carry = 0;
        while (!s1.isEmpty() || !s2.isEmpty()) {
            int val1 = s1.isEmpty() ? 0 : s1.pop().val;
            int val2 = s2.isEmpty() ? 0 : s2.pop().val;
            
            int val = val1 + val2 + carry;
            ListNode node = new ListNode(val % 10);
            carry = val / 10;
            s3.push(node);
        }

        if (carry == 1)
            s3.push(new ListNode(1));

        ListNode dummy = new ListNode(0);
        ListNode node = dummy;
        while (!s3.isEmpty()) {
            node.next = s3.pop();
            node = node.next;
        }
        
        return dummy.next;
    }

    public ListNode addTwoNumbers_bad(ListNode l1, ListNode l2) {
        StringBuilder l1_str = new StringBuilder();
        StringBuilder l2_str = new StringBuilder();
        ListNode temp;

        temp = l1;
        while (temp != null) {
            l1_str.append(Integer.toString(temp.val));
            temp = temp.next;
        }

        temp = l2;
        while (temp != null) {
            l2_str.append(Integer.toString(temp.val));
            temp = temp.next;
        }

        String res_str = Long.toString(Long.parseLong(l1_str.toString()) + Long.parseLong(l2_str.toString()));
        char[] res_chars = res_str.toCharArray();
        ListNode res = new ListNode(res_chars[0] - '0');
        temp = res;
        for (int i = 1; i < res_chars.length; i++) {
            temp.next = new ListNode(res_chars[i] - '0');
            temp = temp.next;
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateListNode ope = new OperateListNode();
        ListNode l1 = ope.createListNode(flds[0]);
        ListNode l2 = ope.createListNode(flds[1]);
        System.out.println("l1 = " + ope.listNodeToString(l1));
        System.out.println("l2 = " + ope.listNodeToString(l2));

        long start = System.currentTimeMillis();

        ListNode result = addTwoNumbers(l1, l2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope.listNodeToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
