import java.util.*;

public class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        // 0ms
        List<Integer> pos = new ArrayList<>();
        for (int i = 0; i < s1.length(); i++) {
            if (s1.charAt(i) != s2.charAt(i))
                pos.add(i);
            if (pos.size() > 2)
                return false;
        }
        return pos.size() == 0 || (pos.size() == 2
                                 && s1.charAt(pos.get(0)) == s2.charAt(pos.get(1))
                                 && s1.charAt(pos.get(1)) == s2.charAt(pos.get(0)));
    }

    public boolean areAlmostEqual2(String s1, String s2) {
        // 0ms
        char[] arr_s1 = s1.toCharArray();
        char[] arr_s2 = s2.toCharArray();
        int[] pos = new int[2];
        int count = 0;

        for (int i = 0; i < arr_s1.length; i++) {
            if (arr_s1[i] != arr_s2[i]) {
                if (count >= 2) {
                    return false;
                }
                pos[count++] = i;
            }
        }
        if (count == 0)
            return true;
        if (count == 1)
            return false;

        char temp = arr_s2[pos[0]]; 
        arr_s2[pos[0]] = arr_s2[pos[1]];
        arr_s2[pos[1]] = temp;

        if (Arrays.equals(arr_s1, arr_s2))
            return true;
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String s1 = flds[0];
        String s2 = flds[1];
        System.out.println("s1 = " + s1 + ", s2 = " + s2);

        long start = System.currentTimeMillis();

        boolean result = areAlmostEqual(s1, s2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
