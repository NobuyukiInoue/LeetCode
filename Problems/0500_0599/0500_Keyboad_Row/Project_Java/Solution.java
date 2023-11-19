import java.util.*;

public class Solution {
    public String[] findWords(String[] words) {
        // 0ms
        int[] rowMap = new int[26];
        String[] rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (int i = 0; i < rows.length; i++) {
            for (char ch : rows[i].toCharArray()) {
                rowMap[ch - 'a'] = i;
            }
        }
        List<String> result = new ArrayList<>();
        for (String word : words) {
            int row = rowMap[word.toLowerCase().charAt(0) - 'a'];
            boolean onSameRow = true;
            for (char ch : word.toLowerCase().toCharArray()) {
                if (rowMap[ch - 'a'] != row) {
                    onSameRow = false;
                    break;
                }
            }
            if (onSameRow) {
                result.add(word);
            }
        }
        return result.toArray(new String[0]);
    }

    public void Main(String temp) {
        String[] words = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").split(",");

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        String[] result = findWords(words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.stringArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
