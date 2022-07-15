import java.util.*;

public class Solution {
    public boolean evaluateTree(TreeNode root) {
        // 0ms - 1ms
        return helper(root);
    }

    private boolean helper(TreeNode node) {
        switch (node.val) {
        case 0:
            return false;
        case 1:
            return true;
        case 2:
            return helper(node.left) || helper(node.right);
        case 3:
            return helper(node.left) && helper(node.right);
        default:
            return true;
        }
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

        boolean result = evaluateTree(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
