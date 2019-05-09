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
        String[] nums1 = flds[0].split(",");
        String[] nums2 = flds[1].split(",");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode p = ope_t.set_TreeNode(nums1);
        TreeNode q = ope_t.set_TreeNode(nums2);
        System.out.print("p = \n" + ope_t.output_TreeNode(p));
        System.out.print("q = \n" + ope_t.output_TreeNode(q));
        System.out.println("p = " + ope_t.Tree2str(p));
        System.out.println("q = " + ope_t.Tree2str(q));

        long start = System.currentTimeMillis();

        boolean result = isSameTree(p, q);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
