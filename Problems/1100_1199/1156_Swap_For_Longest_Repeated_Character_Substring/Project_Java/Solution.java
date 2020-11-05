public class Solution {
    public int maxRepOpt1(String text) {
        // 2ms
        int[] dic = new int[26];
        int max = 0;
        for (char c : text.toCharArray()) {
            dic[c - 'a']++;
            max = Math.max(max, dic[c - 'a']);
        }

        if (max <= 1)
            return max;
        max = 1;
        int n = text.length();
        int j, k;
        for (int i = 0; i < n; i = j) {
            char cur = text.charAt(i);
            for (j = i; j < n && text.charAt(j) == cur; j++);
            for (k = j + 1; k < n && text.charAt(k) == cur; k++);
            if (k - i - 1 == dic[cur - 'a']) {
                max = Math.max(max, k - i - 1);
            } else {
                max = Math.max(max, k - i);
            }
        }

        return max;
    }

    public void Main(String temp) {
        String text = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("text = " + text);

        long start = System.currentTimeMillis();

        int result = maxRepOpt1(text);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
