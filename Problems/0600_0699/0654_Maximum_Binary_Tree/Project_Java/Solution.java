import java.util.*;

public class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        // 2ms
        if (nums.length == 0)
            return null;
        return constructMaximumBinaryTree(nums, 0, nums.length);
    }

    public TreeNode constructMaximumBinaryTree(int[] nums, int start, int end) {
        if (start >= end)
            return null;
        int pos = maxnode(nums, start, end);
        TreeNode node = new TreeNode(nums[pos]);
        node.left = constructMaximumBinaryTree(nums, start, pos);
        node.right = constructMaximumBinaryTree(nums, pos + 1, end);
        return node;
    }

    private int maxnode(int[] nums, int start, int end) {
        int maxnum = Integer.MIN_VALUE;
        int pos = -1;
        for (int i = start; i < end; i++) {
            if (nums[i] > maxnum) {
                maxnum = nums[i];
                pos = i;
            }
        }
        return pos;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);

        long start = System.currentTimeMillis();

        TreeNode result = constructMaximumBinaryTree(nums);

        long end = System.currentTimeMillis();

        OperateTreeNode ope_t = new OperateTreeNode();
        System.out.print("result = \n" + ope_t.treeToStaircaseString(result));
        System.out.println("result = " + ope_t.tree2str(result));
        System.out.println((end - start)  + "ms\n");
    }
}
