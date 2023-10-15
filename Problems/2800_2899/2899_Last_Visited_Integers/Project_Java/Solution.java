import java.util.*;

public class Solution {
    public List<Integer> lastVisitedIntegers(List<String> words) {
        // 3ms
        Stack<Integer> st = new Stack<>();
        int count = 0;
        List<Integer> ans = new ArrayList<>();
        for (String word : words) {
            if (word.equals("prev")) {
                count++;
                if (count <= st.size()) {
                    ans.add(st.get(st.size() - count));
                } else {
                    ans.add(-1);
                }
            } else {
                st.add(Integer.parseInt(word));
                count = 0;
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();
        List<String> words = ml.stringArrayToListStringArray(flds);

        System.out.println("words = " + ml.listStringArrayToString(words));

        long start = System.currentTimeMillis();

        List<Integer> result = lastVisitedIntegers(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
