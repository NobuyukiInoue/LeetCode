import java.util.*;

public class Solution {
    public int countPrefixSuffixPairs(String[] words) {
        // 2ms
        int ans = 0;
        for (int i = 0; i < words.length - 1; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if (words[j].startsWith(words[i]) && words[j].endsWith(words[i])) {
                    ans++;
                }
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        int result = countPrefixSuffixPairs(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
