import java.util.*;

public class Solution {
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        if (root.left != null && root.right != null) {
            int l = minDepth(root.left) + 1;
            int r = minDepth(root.right) + 1;
            return Math.min(l, r);
        } else if (root.left != null) {
            return minDepth(root.left) + 1;
        } else if (root.right != null) {
            return minDepth(root.right) + 1;
        } else {
            return 1;
        }   
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        int result = minDepth(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
