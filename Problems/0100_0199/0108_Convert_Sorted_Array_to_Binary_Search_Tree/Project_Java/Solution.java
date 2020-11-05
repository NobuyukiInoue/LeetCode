import java.util.*;

public class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return sortedArrayToBST_sub(nums, 0, nums.length-1);
    }
    
    public TreeNode sortedArrayToBST_sub(int[] nums, int left, int right) {
        if (left > right)
            return null;
        int mid = (right + left)/2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = sortedArrayToBST_sub(nums, left, mid - 1);
        root.right = sortedArrayToBST_sub(nums, mid+1, right);
        return root;
    }

    public TreeNode sortedArrayToBST2(int[] nums) {
        // 1ms
        if (nums.length == 0)
            return null;
        int pos = nums.length / 2;
        TreeNode node = new TreeNode(nums[pos]);
        if (pos > 0)
            node.left = sortedArrayToBST(Arrays.copyOfRange(nums, 0, pos));
        if (pos > 0 && pos + 1 < nums.length)
            node.right = sortedArrayToBST(Arrays.copyOfRange(nums, pos + 1, nums.length));
        return node;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);

        long start = System.currentTimeMillis();

        TreeNode result = sortedArrayToBST(nums);

        long end = System.currentTimeMillis();

        OperateTreeNode ope_t = new OperateTreeNode();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
