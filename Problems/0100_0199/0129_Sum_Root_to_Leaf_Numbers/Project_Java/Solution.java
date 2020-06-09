import java.util.*;

public class Solution {
    // 0ms
    public int sumNumbers(TreeNode root) {
        return sumNumbers(root, 0);   
    }

    public int sumNumbers(TreeNode node, int sumVal) {
        if (node == null)
            return sumVal;

        sumVal = sumVal*10 + node.val;
        if (node.left == null && node.right == null)
            return sumVal;

        int sumLeft = 0, sumRight = 0;

        if (node.left != null)
            sumLeft = sumNumbers(node.left, sumVal);
        if (node.right != null)
            sumRight = sumNumbers(node.right, sumVal);

        return sumLeft + sumRight;
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

        int result = sumNumbers(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
