import java.util.*;

public class Solution {
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        // 20ms
        List<TreeNode> res = new LinkedList<>();
        postorder(root, new HashMap<>(), res);
        return res;
    }

    public String postorder(TreeNode cur, Map<String, Integer> map, List<TreeNode> res) {
        if (cur == null)
            return "#";  
        String serial = cur.val + "," + postorder(cur.left, map, res) + "," + postorder(cur.right, map, res);
        map.put(serial, map.getOrDefault(serial, 0) + 1);
        if (map.get(serial) == 2)
            res.add(cur);
        return serial;
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

        List<TreeNode> result = findDuplicateSubtrees(root);

        long end = System.currentTimeMillis();

        System.out.print("result = [");
        for (int i = 0; i < result.size(); i++) {
            if (i == 0)
                System.out.print(" [" + ope_t.tree2str(result.get(i)) + "]");
            else
                System.out.print(", [" + ope_t.tree2str(result.get(i)) + "]");
        }
        System.out.println(" ]");
        System.out.println((end - start)  + "ms\n");
    }
}
