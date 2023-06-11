public class Solution {
    public String decodeAtIndex(String s, int k) {
        // 0ms
        int i;
        long tape_length = 0;
        for (i = 0; tape_length < k; i++) {
            tape_length = Character.isDigit(s.charAt(i)) ? tape_length * (s.charAt(i) - '0') : tape_length + 1;
        }
        for (i--; i > 0; i--) {
            if (Character.isDigit(s.charAt(i))) {
                tape_length /= s.charAt(i) - '0';
                k %= tape_length;
            }
            else {
                if (k % tape_length == 0) {
                    break;
                }
                tape_length--;
            }
        }
        return Character.toString(s.charAt(i));
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        String s = flds[0];
        int k = Integer.parseInt(flds[1]);
        System.out.println("s = " + s + ", k = " + k);

        long start = System.currentTimeMillis();

        String result = decodeAtIndex(s, k);

        long end = System.currentTimeMillis();

        System.out.println("result = \"" + result + "\"");
        System.out.println((end - start)  + "ms\n");
    }
}
