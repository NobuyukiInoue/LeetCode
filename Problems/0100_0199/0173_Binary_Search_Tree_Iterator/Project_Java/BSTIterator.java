import java.util.*;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class BSTIterator {
    // 16ms
    int index;
    List<Integer> nums;

    public BSTIterator(TreeNode root) {
        nums = new ArrayList<>();
        dfs(root);
        index = 0;
    }
    
    private void dfs(TreeNode node) {
        if (node == null)
            return;
        if (node.left != null)
            dfs(node.left);
        nums.add(node.val);
        if (node.right != null)
            dfs(node.right);
    }

    /** @return the next smallest number */
    public int next() {
        if (index < nums.size())
            return nums.get(index++);
        return -1;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        if (index < nums.size())
            return true;
        return false;
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
