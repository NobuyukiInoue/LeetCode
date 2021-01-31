import java.util.*;

public class Solution {
    public TreeNode removeLeafNodes(TreeNode root, int target) {
        // 0ms
        if (root == null)
            return null;
        if (root.left != null)
            root.left = removeLeafNodes(root.left, target);
        if (root.right != null)
            root.right = removeLeafNodes(root.right, target);
        if (root.val == target && root.left == null && root.right == null)
            root = null;
        return root;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds[0]);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        int target = Integer.parseInt(flds[1]);
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        TreeNode result = removeLeafNodes(root, target);

        long end = System.currentTimeMillis();

        Codec codec = new Codec();
        System.out.println("result = [" + codec.serialize(result) + "]");
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
