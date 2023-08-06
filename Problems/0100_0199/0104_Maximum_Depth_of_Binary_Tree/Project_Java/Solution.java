import java.util.*;

public class Solution {
    public int maxDepth(TreeNode root) {
        // 0ms
        if (root == null) {
            return 0;
        }
        int max_l = maxDepth(root.left);
        int max_r = maxDepth(root.right);
        return max_l > max_r? max_l + 1: max_r + 1;
    }

    public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root;
        if (flds.equals("")) {
            root = null;
        } else {
            root = ope_t.createTreeNode(flds);
        }
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        int result = maxDepth(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
