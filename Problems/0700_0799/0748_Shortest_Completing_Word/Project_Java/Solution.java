import java.util.*;

public class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        int[] freq = new int[26];
        for (char c: licensePlate.toLowerCase().toCharArray()) {
            if (Character.isLowerCase(c))
                freq[c-'a']++;
        }

        String res="";
        for (String s: words) {
            if ((res.length()==0 || s.length()<res.length()) && ok(Arrays.copyOf(freq, 26), s))
                res = s;
        }

        return res;
    }

    public boolean ok(int[] freq, String s) {
        for (char c: s.toCharArray())
            freq[c-'a']--;
        for (int f: freq)
            if (f>0)
                return false;
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String licensePlate = flds[0];
        String[] words = flds[1].split(",");

        Mylib ml = new Mylib();
        System.out.println("licensePlate = " + licensePlate);
        System.out.println("words[] = " + ml.stringArrayToString(words));

        long start = System.currentTimeMillis();

        String result = shortestCompletingWord(licensePlate, words);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
