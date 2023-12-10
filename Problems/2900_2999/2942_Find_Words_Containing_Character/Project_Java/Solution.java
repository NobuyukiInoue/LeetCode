import java.util.*;

public class Solution {
    public List<Integer> findWordsContaining(String[] words, char x) {
        // 1ms
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < words.length; i++) {
            if (words[i].indexOf(x) != -1) {
                ans.add(i);
            }
        }
        return ans;
    }
    public List<Integer> findWordsContaining2(String[] words, char x) {
        // 2ms
        List<Integer> ans = new ArrayList<>();
        String xStr = Character.toString(x);
        for (int i = 0; i < words.length; i++) {
            if (words[i].contains(xStr)) {
                ans.add(i);
            }
        }
        return ans;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
 
        Mylib ml = new Mylib();
        String[] words = flds[0].split(",");
        char x = flds[1].toCharArray()[0];
        System.out.println("words = " + ml.stringArrayToString(words) + ", x = " + x);

        long start = System.currentTimeMillis();

        List<Integer> result = findWordsContaining(words, x);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
