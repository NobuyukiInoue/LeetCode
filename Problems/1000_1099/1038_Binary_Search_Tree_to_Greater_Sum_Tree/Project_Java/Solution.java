import java.util.*;

public class Solution {
    // 0ms
    private int sum = 0;
    
    public TreeNode bstToGst(TreeNode root) {
        reverseInorderTraversal(root);
        return root;
    }
    
    private void reverseInorderTraversal(TreeNode node) {
        if (node == null) {
            return;
        }
        reverseInorderTraversal(node.right);
        sum += node.val;
        node.val = sum;
        reverseInorderTraversal(node.left);
    }

    public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        TreeNode result = bstToGst(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
