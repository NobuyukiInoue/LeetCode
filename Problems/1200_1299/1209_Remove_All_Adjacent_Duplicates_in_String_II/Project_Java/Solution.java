import java.util.*;

public class Solution {
    public String removeDuplicates(String s, int k) {
        // 17ms - 18ms
        if (s.length() < k) {
            return s;
        }
        List<int[]> st = new ArrayList<>();
        for (char ch : s.toCharArray()) {
            if (!st.isEmpty() && ch == st.get(st.size() - 1)[0]) {
                st.get(st.size() - 1)[1]++;
                if (st.get(st.size() - 1)[1] == k) {
                    st.remove(st.size() - 1);
                }
            } else {
                st.add(new int[] {ch, 1});
            }
        }
        StringBuilder res = new StringBuilder();
        for (int[] pair : st) {
            for (int i = 0; i < pair[1]; i++) {
                res.append((char) pair[0]);
            }
        }
        return res.toString();
    }

    public void Main(String temp) {
        String flds[] = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = \"" + s + "\", k = " + k);

        long start = System.currentTimeMillis();

        String result = removeDuplicates(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
