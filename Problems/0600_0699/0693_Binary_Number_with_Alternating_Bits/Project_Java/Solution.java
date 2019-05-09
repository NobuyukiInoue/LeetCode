public class Solution {
    public boolean hasAlternatingBits(int n) {
        String targetStr = Integer.toBinaryString(n);
    //    System.out.println("targetStr = " + targetStr);
        for (int i = 1; i < targetStr.length(); i++) {
            if (targetStr.charAt(i) == targetStr.charAt(i - 1)) {
                return false;
            }
        }

        return true;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String flds = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(flds);

        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        boolean result = hasAlternatingBits(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
