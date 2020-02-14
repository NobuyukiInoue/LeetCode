import java.util.*;

public class Solution {
    public int maxLength(List<String> arr) {
        // 11ms
        List<Integer> dp = new ArrayList<>();
        dp.add(0);
        int res = 0;
        for (String st : arr) {
            int a = 0, dup = 0;
            for (char ch : st.toCharArray()) {
                dup |= a & (1 << (ch - 'a'));
                a |= 1 << (ch - 'a');
            }
            if (dup > 0)
                continue;
            for (int i = dp.size() - 1; i >= 0; i--) {
                if ((dp.get(i) & a) > 0)
                    continue;
                dp.add(dp.get(i) | a);
                res = Math.max(res, Integer.bitCount(dp.get(i) | a));
            }
        }
        return res;
    }

    private String listArrayToString(List<String> arr) {
        if (arr.size() <= 0)
            return "";
        StringBuffer sb = new StringBuffer("[" + arr.get(0));
        for (int i = 1; i < arr.size(); i++) {
            sb.append(", " + arr.get(i));
        }
        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        List<String> arr = new ArrayList<>();
        for (String fld : flds) {
            arr.add(fld);
        }
        System.out.println("arr = " + listArrayToString(arr));

        long start = System.currentTimeMillis();
        
        int result = maxLength(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
