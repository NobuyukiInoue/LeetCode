import java.util.*;

public class Solution {
    public Node connect(Node root) {
        // 0ms
        if (root == null || root.left == null || root.right == null)
            return root;
        
        root.left.next = root.right;
        if (root.next != null)
            root.right.next = root.next.left;
        
        connect(root.left);
        connect(root.right);
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
