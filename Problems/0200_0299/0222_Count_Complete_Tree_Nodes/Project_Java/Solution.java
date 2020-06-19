import java.util.*;

public class Solution {
    int res = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        // 0ms
        res = Integer.MIN_VALUE;
        oneSideSum(root);
        return res;
    }

    private int oneSideSum(TreeNode node) {
        if (node == null)
            return 0;
        int l = Math.max(0, oneSideSum(node.left));
        int r = Math.max(0, oneSideSum(node.right));
        res = Math.max(res, node.val + l + r);
        return node.val + Math.max(l, r);
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

        int result = maxPathSum(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
