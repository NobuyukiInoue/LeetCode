import java.util.*;

public class Solution {
    int count;
    int res;
    public int kthSmallest(TreeNode root, int k) {
        // 0ms
        count = k;
        res = 0;
        helper(root);
        return res;
    }

    private void helper(TreeNode node) {
        if (node == null)
            return;
        helper(node.left);
        count--;
        if (count == 0) {
            res = node.val;
            return;
        }
        helper(node.right);
    }
/*
    List<Integer> res;
    public int kthSmallest(TreeNode root, int k) {
        // 6ms
        res = new ArrayList<>();
        getVal(root);
        Integer[] res2 = res.toArray(new Integer[res.size()]);
        Arrays.sort(res2);
        return res2[k - 1];
    }

    private void getVal(TreeNode node) {
        if (node == null)
            return;
        res.add(node.val);
        if (node.left != null)
            getVal(node.left);
        if (node.right != null)
            getVal(node.right);
        return;
    }
*/

public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(flds[0].split(","));
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        int k = Integer.parseInt(flds[1]);
        System.out.println("k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int result = kthSmallest(root, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
