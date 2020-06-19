public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p == null || q == null) {
            return false;
        }

        if (p.val == q.val) {
            if (isSameTree(p.left, q.left)) {
                return isSameTree(p.right, q.right);
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode p = ope_t.createTreeNode(flds[0]);
        TreeNode q = ope_t.createTreeNode(flds[1]);
    //  Codec codec = new Codec();
    //  TreeNode p = codec.deserialize(flds[0]);
    //  TreeNode q = codec.deserialize(flds[1]);
        System.out.print("p = \n" + ope_t.treeToStaircaseString(p));
        System.out.print("q = \n" + ope_t.treeToStaircaseString(q));
        System.out.println("p = " + ope_t.tree2str(p));
        System.out.println("q = " + ope_t.tree2str(q));

        long start = System.currentTimeMillis();

        boolean result = isSameTree(p, q);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
