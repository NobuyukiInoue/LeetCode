import java.util.*;

public class Solution {
    public List<String> stringMatching(String[] words) {
        // 3ms
        Set<String> set = new HashSet<>();
        int n = words.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j == i)
                    continue;
                if (words[j].contains(words[i])) {
                    set.add(words[i]);
                    break;
                }
            }
        }
        return new ArrayList<>(set);
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        List<String> result = stringMatching(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listStringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
