public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        // 4ms
        if (root == p || root == q)
            return root;
        if (root == null)
            return null;

        TreeNode leftNode = lowestCommonAncestor(root.left, p, q);
        TreeNode rightNode = lowestCommonAncestor(root.right, p, q);

        if (leftNode != null && rightNode != null)
            return root;
        if (leftNode != null)
            return leftNode;

        return rightNode;
    }

    private TreeNode set_target_node(TreeNode node, int target) {
        if (node == null)
            return null;
        if (node.val == target)
            return node;

        TreeNode leftNode = set_target_node(node.left, target);
        if (leftNode != null)
            return leftNode;

        TreeNode rightNode = set_target_node(node.right, target);
        if (rightNode != null)
            return rightNode;

        return null;
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

        TreeNode p = set_target_node(root, Integer.parseInt(flds[1]));
        TreeNode q = set_target_node(root, Integer.parseInt(flds[2]));
        System.out.println("p = " + ope_t.tree2str(p) + ", q = " + ope_t.tree2str(q));

        long start = System.currentTimeMillis();

        TreeNode result = lowestCommonAncestor(root, p, q);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
