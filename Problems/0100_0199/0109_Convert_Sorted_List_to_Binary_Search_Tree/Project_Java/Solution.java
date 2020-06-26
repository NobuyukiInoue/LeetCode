import java.util.*;

public class Solution {
    public TreeNode sortedListToBST(ListNode head) {
        // 1ms
        if (head == null)
            return null;
        if (head.next == null)
            return new TreeNode(head.val);

        ListNode fast = head;
        ListNode slow = head;

        if (fast != null && fast.next != null)
            fast = fast.next.next;
        
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        TreeNode node = new TreeNode(slow.next.val);
        node.right = sortedListToBST(slow.next.next);
        slow.next = null;
        node.left = sortedListToBST(head);

        return node;
    }

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateListNode ope_l = new OperateListNode();
        ListNode head = ope_l.createListNode(flds);

        long start = System.currentTimeMillis();

        TreeNode result = sortedListToBST(head);

        long end = System.currentTimeMillis();

        OperateTreeNode ope_t = new OperateTreeNode();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
