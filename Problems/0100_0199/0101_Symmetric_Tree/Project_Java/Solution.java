public class Solution {
    public Boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;
        return checkSymmetric(root.left, root.right);
    }

    public Boolean checkSymmetric(TreeNode temp1, TreeNode temp2) {
        if (temp1 == null && temp2 == null)
            return true;
        if (temp1 == null || temp2 == null)
            return false;
        if (temp1.val != temp2.val)
            return false;
        return ( checkSymmetric(temp1.left, temp2.right) && checkSymmetric(temp1.right, temp2.left) );
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

    	boolean result = isSymmetric(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
