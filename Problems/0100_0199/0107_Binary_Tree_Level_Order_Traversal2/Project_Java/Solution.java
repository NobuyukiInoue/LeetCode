import java.util.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Solution {
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        // 1ms
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (root == null)
            return result;
        
        Deque<TreeNode> queue = new ArrayDeque<TreeNode>();
        queue.add(root);
        
        while (true) {
            int nodeCount = queue.size();
            if (nodeCount == 0)
                break;
            
            List<Integer> subList = new ArrayList<Integer>();
            while (nodeCount > 0) {
                TreeNode dataNode = queue.remove();
                subList.add(dataNode.val);
                
                if (dataNode.left != null)
                    queue.add(dataNode.left);
                if (dataNode.right != null)
                    queue.add(dataNode.right);
                
                nodeCount--;
            }
            
            result.add(0, subList);
        }
        
        return result;
    }

    private String listlistArrayToString(List<List<Integer>> flds) {
        if (flds.size() <= 0)
            return "";
        StringBuilder sb = new StringBuilder();
        sb.append("[" + listArrayToString(flds.get(0)));
        for (int i = 1; i < flds.size(); i++)
            sb.append(", " + listArrayToString(flds.get(i)));

        return sb.append("]").toString();
    }

    private String listArrayToString(List<Integer> flds) {
        if (flds.size() <= 0)
            return "";
        StringBuilder sb = new StringBuilder();
        sb.append("[" + Integer.toString(flds.get(0)));
        for (int i = 1; i < flds.size(); i++)
            sb.append(", " + Integer.toString(flds.get(i)));

        return sb.append("]").toString();
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        String[] nums = flds.split(",");

        Operate_TreeNode ope_t = new Operate_TreeNode();
        TreeNode root;
        
        if (flds.length() > 0) {
            root = ope_t.set_TreeNode(nums);
        } else {
            root = null;
        }
        System.out.print("root = \n" + ope_t.output_TreeNode(root));
        System.out.println("root = " + ope_t.Tree2str(root));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = levelOrderBottom(root);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listlistArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
