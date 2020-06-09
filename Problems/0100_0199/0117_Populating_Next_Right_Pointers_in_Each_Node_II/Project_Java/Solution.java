import java.util.*;

public class Solution {
    public Node connect(Node root) {
        // 0ms
        Node node = root;
        Node tail = new Node(0);
        Node dummy = tail;
        while (node != null) {
            tail.next = node.left;
            if (tail.next != null)
                tail = tail.next;
            tail.next = node.right;
            if (tail.next != null)
                tail = tail.next;
            node = node.next;
            if (node == null) {
                tail = dummy;
                node = dummy.next;
            }
        }
        return root;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        String[] nums = flds.split(",");

        Operate_Node ope_t = new Operate_Node();
        Node root = ope_t.set_Node(nums);
        System.out.print("root = \n" + ope_t.output_Node(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        Node result = connect(root);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.output_Node_with_next(result));
        System.out.println("result = " + ope_t.Tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
