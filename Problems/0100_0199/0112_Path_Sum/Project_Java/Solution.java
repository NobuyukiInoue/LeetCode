public class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        // 0ms
        if (root == null) {
            return false;
        }
        if (root.left == null && root.right == null) {
            return (root.val == targetSum);
        }
        if (root.left != null) {
            if (hasPathSum(root.left, targetSum - root.val)) {
                return true;
            }
        }
        if (root.right != null) {
            if (hasPathSum(root.right, targetSum - root.val)) {
                return true;
            }
        }
        return false;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds[0]);
        int targetSum = Integer.parseInt(flds[1]);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));
        System.out.println("targetSum = " + targetSum);

        long start = System.currentTimeMillis();

        boolean result = hasPathSum(root, targetSum);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
