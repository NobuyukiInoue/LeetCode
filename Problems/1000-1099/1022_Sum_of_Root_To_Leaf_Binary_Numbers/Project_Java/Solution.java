import java.util.*;

public class Solution {
    public int sumRootToLeaf(TreeNode root) {
        if (root == null)
            return 0;
        return sub_sumRootToLeaf(root, 0);        
    }

    public int sub_sumRootToLeaf(TreeNode node, int val) {
        val = val*2 + node.val;
        if (node.left == node.right)
            return val;
        int l = 0, r = 0;
        if (node.left != null)
            l = sub_sumRootToLeaf(node.left, val);
        if (node.right != null)
            r = sub_sumRootToLeaf(node.right, val);
        return l + r;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(flds);
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        int result = sumRootToLeaf(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
