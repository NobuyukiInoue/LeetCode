import java.util.*;

public class Solution {
    public int totalFruit(int[] tree) {
        // 7ms
        int[] fruits = new int[2];
        int[] count = new int[2];

        for (int i = 0; i < 2; i++) {
            fruits[i] = -1;
            count[i] = 0;
        }

        int last_count = 0, last = 1, total = 0;

        for (int t : tree) {
            if (indexOf(fruits, t) >= 0) {
                if (t != fruits[last]) {
                    last = notlast(last);
                    last_count = count[last];
                }
                count[last]++;
            } else {
                total = Math.max(total, arraySum(count));
                count[last] -= last_count;
                last = notlast(last);
                fruits[last] = t;
                count[last] = 1;
                last_count = 0;
            }
        }

        total = Math.max(total, arraySum(count));
        return total;
    }

    private int notlast(int last) {
        if (last == 1)
            return 0;
        return 1;
    }

    private int indexOf(int[] data, int target) {
        for (int i = 0; i < data.length; i++) {
            if (target == data[i]) {
                return i;
            }
        }
        return -1;
    }
    private int arraySum(int[] data) {
        if (data == null)
            return 0;
        if (data.length <= 0)
            return 0;

        int total = data[0];
        for (int i = 1; i < data.length; i++)
            total += data[i];

        return total;
    }

    public int totalFruit2(int[] tree) {
        // 41ms
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        int res = 0, i = 0;
        for (int j = 0; j < tree.length; ++j) {
            count.put(tree[j], count.getOrDefault(tree[j], 0) + 1);
            while (count.size() > 2) {
                count.put(tree[i], count.get(tree[i]) - 1);
                if (count.get(tree[i]) == 0) count.remove(tree[i]);
                i++;
            }
            res = Math.max(res, j - i + 1);
        }
        return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] tree = ml.stringToIntArray(flds);
        System.out.println("tree = " + ml.intArrayToString(tree));

        long start = System.currentTimeMillis();

        int result = totalFruit(tree);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
