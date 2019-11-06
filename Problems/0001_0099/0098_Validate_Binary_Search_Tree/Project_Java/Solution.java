import java.util.*;

public class Solution {
    public boolean isValidBST(TreeNode root) {
        // 0ms
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    private boolean isValidBST(TreeNode root, long min, long max) {
        return root==null || (root.val<max && root.val>min && isValidBST(root.left, min, root.val) && isValidBST(root.right, root.val, max));
    }

    public boolean isValidBST2(TreeNode root) {
        // 1ms
        List<Integer> output = new ArrayList<Integer>();
        inOrder(root, output);
        for (int i = 1; i < output.size(); i++) {
            if (output.get(i - 1) >= output.get(i))
                return false;
        }

        return true;
    }

    private void inOrder(TreeNode root, List<Integer> output) {
        if (root == null)
            return;
        inOrder(root.left, output);
        output.add(root.val);
        inOrder(root.right, output);
    }

    public void Main(String args) {
        args = args.replaceAll("#.*", "");
        args = args.replaceAll("//.*", "");
        if (args.length() == 0)
            return;

        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root = ope_t.set_TreeNode(flds.split(","));
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        boolean result = isValidBST(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
