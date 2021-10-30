import java.util.*;

public class Solution {
    public List<TreeNode> allPossibleFBT(int n) {
        // 2ms
        List<TreeNode> ans = new ArrayList<>();
        if (n % 2 == 0) 
            return ans;
        if (n == 1) {
            ans.add(new TreeNode(0));
            return ans;
        }
        for (int i = 1; i < n; i += 2) {
            List<TreeNode> Ll = allPossibleFBT(i);
            List<TreeNode> Lr = allPossibleFBT(n - 1 - i);
            for (TreeNode node_l : Ll)
                for (TreeNode node_r : Lr) {
                    TreeNode node = new TreeNode(0);
                    node.left = node_l;
                    node.right = node_r;
                    ans.add(node);
                }
        }
        return ans;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.print("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        List<TreeNode> result = allPossibleFBT(n);

        long end = System.currentTimeMillis();

        Codec codec = new Codec();
        for (int i = 0; i < result.size(); i++) {
            if (i == 0)
                System.out.print("result = [[" + codec.serialize(result.get(i)) + "]");
            else
                System.out.print(",[" + codec.serialize(result.get(i)) + "]");
        }
        System.out.println("]");

        OperateTreeNode ope_t = new OperateTreeNode();
        for (int i = 0; i < result.size(); i++) {
            System.out.print("result[" + Integer.toString(i) + "] = \n" + ope_t.treeToStaircaseString(result.get(i)));
        }
        System.out.println();

        for (int i = 0; i < result.size(); i++) {
            System.out.println("result[" + Integer.toString(i) + "] = " + ope_t.tree2str(result.get(i)));
        }
        System.out.println();

        System.out.println((end - start)  + "ms\n");
    }
}
