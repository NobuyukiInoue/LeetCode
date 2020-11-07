import java.util.*;

public class Solution {
    public TrieNode root = new TrieNode();

    public int findMaximumXOR(int[] nums) {
        // 17ms
        for (int num: nums) {
            TrieNode walker = root;
            for (int i = 31; i >= 0; i--) {
                int j = (num >> i) & 1;
                if (walker.children[j] == null)
                    walker.children[j] = new TrieNode();
                walker = walker.children[j];
            }
            walker.num = num;
        }

        TrieNode iWalker = root;
        TrieNode jWalker = root;
        return dfs(iWalker, jWalker, 31);
    }

    public int dfs(TrieNode iWalker, TrieNode jWalker, int index) {
        if (iWalker == null || jWalker == null) return 0;
        if (index < 0) return iWalker.num ^ jWalker.num;

        index--;
        if (iWalker.children[0] != null && jWalker.children[1] != null || iWalker.children[1] != null && jWalker.children[0] != null) {
            return Math.max(dfs(iWalker.children[0], jWalker.children[1], index), dfs(iWalker.children[1], jWalker.children[0], index));
        } else {
            return Math.max(dfs(iWalker.children[1], jWalker.children[1], index), dfs(iWalker.children[0], jWalker.children[0], index));
        }
    }

    class TrieNode {
        public TrieNode[] children;
        public int num;
        
        public TrieNode() {
            children = new TrieNode[2];
        }
    }

    public int findMaximumXOR2(int[] nums) {
        // 111ms
        int max = 0, mask = 0;
        for (int i = 31; i >= 0; i--) {
            mask = ~((1 << i) - 1);
            int tmp = max | (1 << i);
            Set<Integer> set = new HashSet<Integer>();
            for (int num: nums) {
                int val = num & mask;
                if(set.contains(tmp ^ val))
                    max = Math.max(max, tmp);
                set.add(val);
            }
        }
        return max;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int result = findMaximumXOR(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
