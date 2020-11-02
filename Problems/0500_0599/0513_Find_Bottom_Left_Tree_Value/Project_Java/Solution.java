import java.util.*;

public class Solution {
    public int findBottomLeftValue(TreeNode root) {
        // 0ms
        return findBottomLeftValue(root, 1, new int[]{0,0});
    }

    public int findBottomLeftValue(TreeNode root, int depth, int[]res) {
        if (res[1] < depth) {
            res[0] = root.val;
            res[1] = depth;
        }
        if (root.left != null)
            findBottomLeftValue(root.left, depth + 1, res);
        if (root.right != null)
            findBottomLeftValue(root.right, depth + 1, res);
        return res[0];
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

        int result = findBottomLeftValue(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
