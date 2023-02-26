import java.util.*;

public class Solution {
    // 0ms
    int maxDiff;
    public int maxAncestorDiff(TreeNode root) {
        maxDiff = 0;
        maxAncestorDiff(root, root.val, root.val);
        return maxDiff;
    }

    public void maxAncestorDiff(TreeNode node, int v_min, int v_max) {
        if (node == null) {
            return;
        }
        maxDiff = Math.max(maxDiff, Math.abs(v_min - node.val));
        maxDiff = Math.max(maxDiff, Math.abs(v_max - node.val));
        v_min = Math.min(v_min, node.val);
        v_max = Math.max(v_max, node.val);
        maxAncestorDiff(node.left, v_min, v_max);
        maxAncestorDiff(node.right, v_min, v_max);
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

        int result = maxAncestorDiff(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
