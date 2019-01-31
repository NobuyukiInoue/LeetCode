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
}
