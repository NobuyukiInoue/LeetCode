import java.util.*;

public class Solution {
    public boolean checkTree(TreeNode root) {
        // 0ms
        return root.val == root.left.val + root.right.val;        
    }

    public void Main(String args) {
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        boolean result = checkTree(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
