import java.util.*;

public class Solution {
    public Node copyRandomList(Node head) {
        // 0ms
        if (head == null) {
            return null;
        }

        Node cur = head;
        while (cur != null) {
            Node next = cur.next;
            cur.next = new Node(cur.val);
            cur.next.next = next;
            cur = next;
        }
		
        cur = head;
        while (cur != null) {
            if (cur.random != null)
                cur.next.random = cur.random.next;
            cur = cur.next.next;
        }
		
        cur = head;
        Node copyHead = head.next;
        while (cur != null) {
            Node next = cur.next.next;
            Node copy = cur.next;
            cur.next = next;
            if (next != null)
                copy.next = next.next;
            cur = next;
        }
        return copyHead;
    }

    // 0ms - 1ms
    Map<Node,Node> map = new HashMap<>();
    public Node copyRandomList_recursive(Node head) {
        if(head == null) {
            return null;
        }
        Node temp = new Node(head.val);
        map.put(head,temp);
        temp.next = copyRandomList_recursive(head.next);
        temp.random = map.get(head.random);
        return temp;
   }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateNode ope_n = new OperateNode();
        Node head;
        if (flds[0].equals("[]") || flds[0].length() == 0) {
            head = null;
        } else {
            head = ope_n.createNode(flds);
        }
        System.out.println("head = [" + ope_n.nodeToString(head) + "]");

        long start = System.currentTimeMillis();

        Node result = copyRandomList(head);

        long end = System.currentTimeMillis();

        System.out.println("result = [" + ope_n.nodeToString(result) + "]");
        System.out.println((end - start)  + "ms\n");
    }
}
