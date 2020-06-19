public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root.val > p.val && root.val > q.val) {
            return lowestCommonAncestor(root.left, p, q);
        } else if(root.val < p.val && root.val < q.val) {
            return lowestCommonAncestor(root.right, p, q);
        } else {
            return root;
        }
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

        TreeNode p = ope_t.createTreeNode(flds[1]);
        TreeNode q = ope_t.createTreeNode(flds[2]);
        System.out.println("p = " + ope_t.tree2str(p) + ", q = " + ope_t.tree2str(q));

        long start = System.currentTimeMillis();

        TreeNode result = lowestCommonAncestor(root, p, q);

        long end = System.currentTimeMillis();

        System.out.println("root = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
