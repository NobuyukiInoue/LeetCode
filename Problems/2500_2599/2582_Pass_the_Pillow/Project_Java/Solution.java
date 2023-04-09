public class Solution {
    public int passThePillow(int n, int time) {
        // 0ms
        return n - Math.abs(n - 1 - time % (n * 2 - 2));
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int time = Integer.parseInt(flds[1]);
        System.out.println("n = " + n);
        System.out.println("time = " + time);

        long start = System.currentTimeMillis();

        int result = passThePillow(n, time);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
