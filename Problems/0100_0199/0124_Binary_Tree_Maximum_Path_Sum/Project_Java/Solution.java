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

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(flds.split(","));
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        int result = maxPathSum(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
