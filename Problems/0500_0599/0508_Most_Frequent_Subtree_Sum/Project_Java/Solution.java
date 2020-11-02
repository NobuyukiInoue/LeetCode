import java.util.*;

public class Solution {
    Map<Integer, Integer> count = new HashMap<Integer, Integer>();
    int maxCount = 0;
    public int[] findFrequentTreeSum(TreeNode root) {
        // 6ms
        dfs(root);
        List<Integer> res = new ArrayList<>();
        for (int currentSum : count.keySet()) {
            if (count.get(currentSum) == maxCount)
                res.add(currentSum);
        }
        return res.stream().mapToInt(i->i).toArray();        
    }

    private int dfs(TreeNode node) {
        if (node == null)
            return 0;
        int currentSum = node.val + dfs(node.left) + dfs(node.right);
        count.put(currentSum, count.getOrDefault(currentSum, 0) + 1);
        maxCount = Math.max(maxCount, count.get(currentSum));
        return currentSum;
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

        int[] result = findFrequentTreeSum(root);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
