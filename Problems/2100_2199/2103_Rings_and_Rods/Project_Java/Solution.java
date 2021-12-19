import java.util.*;

import org.xml.sax.HandlerBase;

public class Solution {
    public int countPoints(String rings) {
        // 0ms
        HashMap<Character, Integer>[] rods = new HashMap[10];
        for (int i = 0; i < 10; i++) {
            rods[i] = new HashMap<>();
        }

        for (int i = 0; i < rings.length(); i += 2) {
            rods[rings.charAt(i + 1) - '0'].put(rings.charAt(i), 1);
        }

        int ans = 0;
        for (int i = 0; i < 10; i++) {
            if (rods[i].size() >= 3) {
                ans++;
            }
        }
        return ans;
    }
    
    public void Main(String temp) {
        String rings = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("rings = " + rings);

        long start = System.currentTimeMillis();

        int result = countPoints(rings);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
