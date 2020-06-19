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

        OperateNode ope_n = new OperateNode();
        Node root = ope_n.createNode(flds);
        System.out.print("root = \n" + ope_n.treeToStaircaseString(root));
        System.out.println("root = " + ope_n.tree2str(root));

        long start = System.currentTimeMillis();

        Node result = connect(root);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_n.treeToStaircaseString_with_next(result));
        System.out.println("result = " + ope_n.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
