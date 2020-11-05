import java.util.*;

public class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        String base = words[0];
        int index = 0;
        for(int i = 1; i < words.length; i++) {
            int min = Math.min(base.length(), words[i].length());
            while(index < min && base.charAt(index) == words[i].charAt(index)) {
                index++;
            }
            if(index == words[i].length()) return false;
            if(order.indexOf(base.charAt(index)) > order.indexOf(words[i].charAt(index))) {
                return false;
            } else {
                base = words[i];
            }
        }
        return true;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String[] words = flds[0].split(",");
        String order = flds[1];

        Mylib ml = new Mylib();
        System.out.println("words = " + ml.stringArrayToString(words) + ", order = " + order);

        long start = System.currentTimeMillis();

        Boolean result = isAlienSorted(words, order);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
