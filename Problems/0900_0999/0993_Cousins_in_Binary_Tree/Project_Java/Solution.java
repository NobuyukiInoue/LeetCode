import java.util.*;

public class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        int[] nums = new int[101];
        dfs(root, nums, 1);
        return nums[x] / 2 != nums[y] / 2 && (int)(Math.log(nums[x]) / Math.log(2)) == (int)(Math.log(nums[y]) / Math.log(2));
    }
    
    private void dfs(TreeNode root, int[] nums, int x) {
        nums[root.val] = x;
        if(root.left != null ) dfs(root.left, nums, 2 * x);
        if(root.right != null ) dfs(root.right, nums, 2 * x + 1);
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
        int x = Integer.parseInt(flds[1]);
        int y = Integer.parseInt(flds[2]);

        long start = System.currentTimeMillis();

        boolean result = isCousins(root, x, y);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
