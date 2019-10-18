import java.util.*;

public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        // 1ms
        return buildTree(inorder, inorder.length - 1, 0, postorder, postorder.length - 1);
    }

    private TreeNode buildTree(int[] inorder, int inStart, int inEnd, int[] postorder, int postStart) {
        if (postStart < 0 || inStart < inEnd)
            return null;
        
        TreeNode root = new TreeNode(postorder[postStart]);
        int rIndex = inStart;

        for (int i = inStart; i >= inEnd; i--) {
            if (inorder[i] == postorder[postStart]) {
                rIndex = i;
                break;
            }
        }

        root.right = buildTree(inorder, inStart, rIndex + 1, postorder, postStart - 1);
        root.left = buildTree(inorder, rIndex - 1, inEnd, postorder, postStart - (inStart - rIndex) - 1);
        return root;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String[] nums1 = flds[0].split(",");
        String[] nums2 = flds[1].split(",");

        int[] inorder = new int[nums1.length];
        for (int i = 0; i < inorder.length; ++i) {
            inorder[i] = Integer.parseInt(nums1[i]);
        }

        int[] postorder = new int[nums2.length];
        for (int i = 0; i < postorder.length; ++i) {
            postorder[i] = Integer.parseInt(nums2[i]);
        }

        Mylib ml = new Mylib();
        System.out.println("inorder = " + ml.intArrayToString(inorder));
        System.out.println("postorder = " + ml.intArrayToString(postorder));

        long start = System.currentTimeMillis();

        TreeNode result = buildTree(inorder, postorder);

        long end = System.currentTimeMillis();

        Operate_TreeNode ope_t = new Operate_TreeNode();
        System.out.print("result = \n" + ope_t.output_TreeNode(result));
        System.out.println("result = " + ope_t.Tree2str(result));

        System.out.println((end - start)  + "ms\n");
    }
}
