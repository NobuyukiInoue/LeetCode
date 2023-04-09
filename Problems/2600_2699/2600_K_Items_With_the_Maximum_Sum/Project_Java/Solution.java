public class Solution {
    public int kItemsWithMaximumSum(int numOnes, int numZeros, int numNegOnes, int k) {
        // 1ms
        return Math.min(k, numOnes) - Math.max(0, k - numZeros - numOnes);
    }
    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int numOnes = Integer.parseInt(flds[0]);
        int numZeros = Integer.parseInt(flds[1]);
        int numNegOnes = Integer.parseInt(flds[2]);
        int k = Integer.parseInt(flds[3]);
        System.out.println("numOnes = " + numOnes + ", numZeros = " + numZeros + ", numNegOnes = " + numNegOnes + ", k = " + k);

        long start = System.currentTimeMillis();

        int result = kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
