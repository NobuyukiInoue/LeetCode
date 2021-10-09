import java.util.*;

public class Solution {
    public TreeNode bstFromPreorder(int[] preorder) {
        // 0ms
        if (preorder == null) {
            return null;
        }
        TreeNode node = new TreeNode(preorder[0]);
        for (int i = 1; i < preorder.length; i++) {
            helper(node, preorder[i]);
        }
        return node;
    }

    private TreeNode helper(TreeNode node, int val) {
        if (node == null) {
            node = new TreeNode(val);
            return node;
        }
        if (val < node.val) {
            node.left = helper(node.left, val);
        } else {
            node.right = helper(node.right, val);
        }
        return node;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        Mylib ml = new Mylib();
        int[] preorder = ml.stringToIntArray(flds);

        long start = System.currentTimeMillis();

        TreeNode result = bstFromPreorder(preorder);

        long end = System.currentTimeMillis();

        OperateTreeNode ope_t = new OperateTreeNode();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
