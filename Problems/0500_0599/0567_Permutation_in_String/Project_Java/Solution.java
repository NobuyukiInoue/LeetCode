import java.util.*;

public class Solution {
    public boolean checkInclusion(String s1, String s2) {
        // 4ms
        if (s1.length() > s2.length())
            return false;

        int leftptr = 0;
        int table1[] = new int[26];
        int table2[] = new int[26];
        int size = s1.length();

        for(int i=0;i<size;i++){
            table1[s1.charAt(i) - 'a']++;
            table2[s2.charAt(i) - 'a']++;
        }
        for (int i = size; i < s2.length(); i++){
            if (check(table1, table2)){
                return true;
            }
            table2[s2.charAt(leftptr) - 'a']--;
            table2[s2.charAt(i) - 'a']++;
            leftptr++;
            
        }
        if (check(table1, table2)) {
                return true;
        }
        return false;
    }
    
    public boolean check(int table1[], int table2[]){
        for (int i = 0; i < 26; i++) {
            if (table1[i] != table2[i])
                return false;
        }
        return true;
    }

    public boolean checkInclusion2(String s1, String s2) {
        // 23ms
        int s1Length = s1.length();
        int s2Length = s2.length();

        if (s1Length > s2Length)
            return false;

        Map<Character, Integer> dic_s1 = new HashMap<>();
        Map<Character, Integer> dic_s2 = new HashMap<>();
        for (char ch : s1.toCharArray()) {
            dic_s1.put(ch, dic_s1.getOrDefault(ch, 0) + 1);
        }

        for (char ch : s2.substring(0, s1Length).toCharArray()) {
            dic_s2.put(ch, dic_s2.getOrDefault(ch, 0) + 1);
        }

        /*
        System.out.println("s1 = " + dic_s1);
        System.out.println("s2 = " + dic_s2);
        */

        if (dic_s1.equals(dic_s2))
            return true;

        for (int i = s1Length; i < s2Length; i++) {
            char ch_pre = s2.charAt(i - s1Length);
            char ch_tail = s2.charAt(i);
            dic_s2.put(ch_tail, dic_s2.getOrDefault(ch_tail, 0) + 1);

            dic_s2.put(ch_pre, dic_s2.get(ch_pre) - 1);
            if (dic_s2.get(ch_pre) == 0) {
                dic_s2.remove(ch_pre);
            }

            if (dic_s1.equals(dic_s2))
                return true;
            /*
            System.out.println("s1 = " + dic_s1);
            System.out.println("s2 = " + dic_s2);
            System.out.println();
            */
        }
        return false;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim().split(",");

        String s1 = flds[0];
        String s2 = flds[1];
        System.out.println("s1 = " + s1);
        System.out.println("s2 = " + s2);

        long start = System.currentTimeMillis();

        boolean result = checkInclusion(s1, s2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
