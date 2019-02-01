public class Solution {
    public static char findTheDifference(String s, String t) {
        int sum = t.charAt(0);

        for(int i = 1; i < t.length(); i++)
            sum = sum + t.charAt(i) - s.charAt(i - 1);

        return (char)sum;
    }

    public static char findTheDifference_bug(String s, String t) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        for(char c : t.toCharArray()) {
            count[c - 'a']--;
        }        
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) return (char) (i + 97);
        }
        return ' ';
    }

    public static char findTheDifference_old(String s, String t) {
        String str = "abcdefghijklmnopqrstuvwxyz";
        String temp;

        for (int i = 0; i < str.length(); ++i) {
            temp = String.valueOf(str.charAt(i));
            if (s.split(temp).length != t.split(temp).length) {
                return str.charAt(i);
            }
        }

        return '0';
    }

    public static void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");
        String s = flds[0];
        String t = flds[1];

        System.out.println("s = " + s + ", t = " + t);

        long start = System.currentTimeMillis();

        char result = findTheDifference(s, t);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
