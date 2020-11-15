import java.util.*;

public class Solution {
    public List<TreeNode> generateTrees(int n) {
        // 1ms
        if (n == 0)
            return new ArrayList<TreeNode>();
        return generate(1, n);
    }

    private List<TreeNode> generate(int left, int right) {
        List<TreeNode> list = new ArrayList<>();

        if (left > right)
            return list;
        if (left == right) {
            list.add(new TreeNode(left));
            return list;
        }

        for (int curr = left; curr <= right; curr++) {
            List<TreeNode> leftChild = generate(left, curr-1);
            List<TreeNode> rightChild = generate(curr+1, right);

            if (leftChild.size() != 0 && rightChild.size() != 0) {
                for (TreeNode leftRoot : leftChild) {
                    for (TreeNode rightRoot : rightChild) {
                        TreeNode currRoot = new TreeNode(curr);
                        currRoot.left = leftRoot;
                        currRoot.right = rightRoot;
                        list.add(currRoot);
                    }
                }
            } else if (leftChild.size() != 0) {
                for (TreeNode leftRoot : leftChild) {
                    TreeNode currRoot = new TreeNode(curr);
                    currRoot.left = leftRoot;
                    list.add(currRoot);
                }
            } else if (rightChild.size() != 0) {
                for (TreeNode rightRoot : rightChild) {
                    TreeNode currRoot = new TreeNode(curr);
                    currRoot.right = rightRoot;
                    list.add(currRoot);
                }
            }
        }
        return list;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        List<TreeNode> result = generateTrees(n);

        long end = System.currentTimeMillis();

        OperateTreeNode ope_t = new OperateTreeNode();
        for (int i = 0; i < result.size(); i++) {
            System.out.print("result[" + Integer.toString(i) + "] = \n" + ope_t.treeToStaircaseString(result.get(i)));
            System.out.println("result[" + Integer.toString(i) + "] = " + ope_t.tree2str(result.get(i)));
        }
        System.out.println((end - start)  + "ms\n");
    }
}
