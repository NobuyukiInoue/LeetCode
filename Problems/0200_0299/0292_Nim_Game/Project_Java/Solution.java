public class Solution {
    public boolean canWinNim(int n) {
        return !(n % 4 == 0);
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String args_str = args.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        Integer n = Integer.parseInt(args_str);

        long start = System.currentTimeMillis();

        boolean result = canWinNim(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
