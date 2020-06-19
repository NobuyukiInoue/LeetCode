public class Solution {
    public TreeNode trimBST(TreeNode root, int L, int R) {
    	if (root != null) {
            if (root.val > R) {
                return trimBST(root.left, L, R);
            } else if (root.val < L) {
                return trimBST(root.right, L, R);
            }
            root.left = trimBST(root.left, L, R);
            root.right = trimBST(root.right, L, R);
            return root;
        }
    
        return root;
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

        TreeNode result = trimBST(root, L, R);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
