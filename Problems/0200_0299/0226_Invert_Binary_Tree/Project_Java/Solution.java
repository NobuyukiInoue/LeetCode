public class Solution {
    public TreeNode invertTree(TreeNode root) {
        if (root == null)
            return null;
        TreeNode t = root.left;
        root.left = root.right;
        root.right = t;
        invertTree(root.left);
        invertTree(root.right);
        return root;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        String[] nums = flds.split(",");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(nums);
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        TreeNode result = invertTree(root);

        long end = System.currentTimeMillis();

        System.out.print("result = \n" + ope_t.output_TreeNode(result));
        System.out.println("result = " + ope_t.Tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
