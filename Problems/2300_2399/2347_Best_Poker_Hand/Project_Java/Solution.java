import java.util.*;

public class Solution {
    public String bestHand(int[] ranks, char[] suits) {
        // 0ms
        int[] cnt = new int[14];
        int cnt_max = 0;
        for (int i : ranks) {
            cnt[i]++;
            cnt_max = Math.max(cnt_max, cnt[i]);
        }
        if (suits[0] == suits[1] && suits[1] == suits[2] && suits[2] == suits[3] && suits[3] == suits[4]) {
            return "Flush";
        } else if (cnt_max >= 3) {
            return "Three of a Kind";
        } else if (cnt_max == 2) {
            return "Pair";
        } else {
            return "High Card";
        } 
    }

    private String charArrayToString(char[] flds) {
        if (flds == null || flds.length == 0) {
            return "";
        }
        StringBuilder sb = new StringBuilder(Character.toString(flds[0]));
        for (int i = 1; i < flds.length; i++) {
            sb.append("," + Character.toString(flds[i]));
        }
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] ranks = Mylib.stringToIntArray(flds[0]); 
        char[] suits = flds[1].replace(",", "").toCharArray();
        System.out.println("ranks = " + ml.intArrayToString(ranks) + ", suits = [" + charArrayToString(suits) + "]");

        long start = System.currentTimeMillis();

        String result = bestHand(ranks, suits);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
