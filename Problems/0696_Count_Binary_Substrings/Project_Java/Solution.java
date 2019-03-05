public class Solution {
    public int countBinarySubstrings(String s) {
        int cur = 1, pre = 0, res = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1))
                cur++;
            else {
                res += Math.min(cur, pre);
                pre = cur;
                cur = 1;
            }
        }
        return res + Math.min(cur, pre);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String s = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        System.out.println("s = " + s);

        long start = System.currentTimeMillis();

        int result = countBinarySubstrings(s);

        long end = System.currentTimeMillis();

        System.out.println("result = " + String.valueOf(result));
        System.out.println((end - start)  + "ms\n");
    }
}
