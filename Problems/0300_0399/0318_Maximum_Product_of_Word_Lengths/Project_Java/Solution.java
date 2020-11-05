import java.util.*;

public class Solution {
    public int maxProduct(String[] words) {
        // 7ms
        int[] bitmask = new int[words.length];
        int index = 0;
        for (String w : words) {
            for (int i = 0; i < w.length(); i++) {
                bitmask[index] |= 1 << w.charAt(i) - 'a';
            }
            index++;
        }

        int max = 0;
        for (int i = 0; i < words.length; i++){
            for (int j = i + 1; j < words.length; j++) {
                if ((bitmask[i] & bitmask[j]) == 0) {
                    max = Math.max(max, words[i].length() * words[j].length());
                }
            }
        }

        return max;
    }

    public void Main(String temp) {
        String[] words  = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        int result = maxProduct(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
