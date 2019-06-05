import java.util.*;

public class Solution {
    public boolean isBalanced(TreeNode root) {
        return isBalanced_Sub(root, 0) >= 0;
    }

    private int isBalanced_Sub(TreeNode root, int height) {
        if (root == null) {
            return height;
        }
        
        int leftTree = isBalanced_Sub(root.left, height + 1);
        int rightTree = isBalanced_Sub(root.right, height + 1);
        if (leftTree < 0 || rightTree < 0 || Math.abs(leftTree - rightTree) > 1) {
            return -1;
        }
        
        return Math.max(leftTree, rightTree);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(flds.split(","));
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        boolean result = isBalanced(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
