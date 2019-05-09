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
        String[] nums1 = flds[0].split(",");
        String[] nums2 = flds[1].split(",");
        String[] nums3 = flds[2].split(",");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(nums1);
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        TreeNode p = ope_t.set_TreeNode(nums2);
        TreeNode q = ope_t.set_TreeNode(nums3);
        System.out.println("p = " + ope_t.Tree2str(p) + ", q = " + ope_t.Tree2str(q));

        long start = System.currentTimeMillis();

        TreeNode result = lowestCommonAncestor(root, p, q);

        long end = System.currentTimeMillis();

        System.out.println("root = " + ope_t.Tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
