import java.util.*;

public class Solution {
    public int numSplits(String s) {
        // 5ms
        int l[] = new int[26], r[] = new int[26], d_l = 0, d_r = 0, res = 0;
        char[] s_arr = s.toCharArray();
        for (char ch : s_arr)
            d_r += ++r[ch - 'a'] == 1 ? 1 : 0;
        for (char ch : s_arr) {
            d_l += ++l[ch - 'a'] == 1 ? 1 : 0;
            d_r -= --r[ch - 'a'] == 0 ? 1 : 0;
            res += d_l == d_r ? 1 : 0;
        }
        return res;
    }

    public int numSplits2(String s) {
        // 18ms - 19ms
        HashMap<Character, Integer> map = new HashMap<>();
        for (char ch : s.toCharArray()) {
            map.put(ch, map.getOrDefault(ch, 0) + 1);
        }

        Integer[] left = new Integer[map.size() + 1];
        int i = 0;
        for (char ch : map.keySet()) {
            left[i++] = s.indexOf(ch);
        }
        left[i] = s.length();
        Arrays.sort(left);

        Integer[] right = new Integer[map.size() + 1];
        i = 0;
        for (char ch : map.keySet()) {
            right[i++] = s.lastIndexOf(ch);
        }
        right[i] = 0;
        Arrays.sort(right, Collections.reverseOrder());

        int ind = 0;
        for (i = 0; i < left.length; i++) {
            if (left[i] <= right[i]) {
                ind = Math.max(ind, i);
            }
        }
        return Math.min(right[ind], left[ind + 1]) - Math.max(left[ind], right[ind + 1]);
    }

    public int numSplits3(String s) {
        // 18ms - 19ms
        int len_s = s.length();
        if (len_s == 1)
            return 0;
        else if (len_s == 2)
            return 1;
        HashMap<Character, Integer> first = new HashMap<>(); 
        HashMap<Character, Integer> last = new HashMap<>();
        int index = 0;
        for (index = 0; index < len_s; index++) {
            if (!first.containsKey(s.charAt(index)))
                first.put(s.charAt(index), index);
            last.put(s.charAt(index), index);
        }
        int[] indices = new int[first.size() + last.size()];
        index = 0;
        for (int v : first.values()) {
            indices[index++] = v;
        }
        for (int v : last.values()) {
            indices[index++] = v;
        }
        Arrays.sort(indices);
        int middle = indices.length / 2;
        return indices[middle] - indices[middle - 1];
    }

    public void Main(String temp) {
        String s = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("s = \"" + s + "\"");

        long start = System.currentTimeMillis();

        int result = numSplits(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
