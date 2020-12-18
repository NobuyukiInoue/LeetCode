import java.util.*;

public class Solution {
    public String minWindow(String s, String t) {
        // 3ms
        int slen = s.length();
        int tlen = t.length();
        int i = 0, j = 0, head = 0;
        int len = (int)1e8;
        int[] freq = new int[128];
        int req = tlen;

        for (int k = 0; k < tlen; k++) {
            freq[t.charAt(k)]++;
        }
        while (j < slen) {
            if(freq[s.charAt(j++)]-- > 0 )
                req--;
            
            while(req == 0) {
                if (j - i < len)
                    len = (j - (head = i));
                
                if (freq[s.charAt(i++)]++ == 0)
                    req++;
            }
        }
        return len < (int)1e8 ? s.substring(head,head + len) : "";
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String s = flds[0];
        String t = flds[1];
        System.out.println("s = " + s + ", t = " + t);

        long start = System.currentTimeMillis();

        String result = minWindow(s, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
