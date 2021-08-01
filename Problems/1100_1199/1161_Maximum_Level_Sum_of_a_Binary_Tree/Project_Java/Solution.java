import java.util.*;

public class Solution {
    // 4ms
    ArrayList<Integer> sums;

    public int maxLevelSum(TreeNode root) {
        sums = new ArrayList<>();
        dfs(root, 0);

        int temp_max = Integer.MIN_VALUE;
        int ans = 0;
        for (int i = 0; i < sums.size(); i++) {
            int temp = sums.get(i);
            if (temp > temp_max) {
                temp_max = temp;
                ans = i;
            }
        }
        return ans + 1;        
    }

    private void dfs(TreeNode node, int level) {
        if (node == null)
            return;
        if (level >= sums.size()) {
            sums.add(node.val);
        } else {
            sums.set(level, sums.get(level) + node.val);
        }
        dfs(node.left, level + 1);
        dfs(node.right, level + 1);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        OperateTreeNode ope_t = new OperateTreeNode();
        TreeNode root = ope_t.createTreeNode(flds);
    //  Codec codec = new Codec();
    //  TreeNode root = codec.deserialize(flds);
        System.out.print("root = \n" + ope_t.treeToStaircaseString(root));
        System.out.println("root = " + ope_t.tree2str(root));

        long start = System.currentTimeMillis();

        int result = maxLevelSum(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
