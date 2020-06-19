import java.util.*;

public class Solution {
    public int rangeSumBST(TreeNode root, int L, int R) {
        if (root==null)
            return 0;
        if (root.val<L)
            return rangeSumBST(root.right, L, R);
        if (root.val>R)
            return rangeSumBST(root.left,L,R);
        return root.val + rangeSumBST(root.left, L, R) + rangeSumBST(root.right, L, R);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds[0]);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds[0]);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));
        int L = Integer.parseInt(flds[1]);
        int R = Integer.parseInt(flds[2]);

        long start = System.currentTimeMillis();

        int result = rangeSumBST(root, L, R);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
