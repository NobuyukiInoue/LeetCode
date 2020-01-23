import java.util.*;

public class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        // 0ms
        List<Integer> resultList = new ArrayList<Integer>();
        helper(root, resultList);
        return resultList;
    }

    private void helper(TreeNode node, List<Integer> resultList) {
        if (node == null)
            return;
        helper(node.left, resultList);
        resultList.add(node.val);
        helper(node.right, resultList);
    }

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
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

        List<Integer> result = inorderTraversal(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}