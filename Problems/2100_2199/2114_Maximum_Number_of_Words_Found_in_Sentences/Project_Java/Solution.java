import java.util.*;

public class Solution {
    public int mostWordsFound(String[] sentences) {
        // 2ms
        int res = 0;
        for (String sentence : sentences) {
            res = Math.max(res, sentence.split(" ").length);
        }
        return res;
    }

    public int mostWordsFound2(String[] sentences) {
        // 4ms
        return Arrays.stream(sentences).mapToInt(s -> s.split(" ").length).max().getAsInt();
    }

    public void Main(String temp) {
        String[] sentences = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");
        Mylib ml = new Mylib();
        System.out.println("sentences = " + ml.stringArrayToString(sentences));

        long start = System.currentTimeMillis();

        int result = mostWordsFound(sentences);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
