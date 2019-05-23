import java.util.*;

public class Solution {
    public TreeNode increasingBST(TreeNode root) {
        return increasingBST(root, null);
    }

    public TreeNode increasingBST(TreeNode root, TreeNode tail) {
        if (root == null)
            return tail;
        TreeNode res = increasingBST(root.left, root);
        root.left = null;
        root.right = increasingBST(root.right, tail);
        return res;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(flds);
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        TreeNode result = increasingBST(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope_t.output_TreeNode(result));
        System.out.println("result = " + ope_t.Tree2str(result) + "\n");
        System.out.println((end - start)  + "ms\n");
    }
}
