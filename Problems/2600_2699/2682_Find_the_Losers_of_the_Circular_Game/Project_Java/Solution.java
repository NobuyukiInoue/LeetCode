public class Solution {
    public int[] circularGameLosers(int n, int k) {
        // 2ms
        boolean[] check = new boolean[n];
        int pre = 0, i;
        
        for (i = 1; !check[pre]; i++) {
          check[pre] = true;
          pre = (pre + i*k) % n;
        }
        int[] ans = new int[n - i + 1];
        int j = 0;
    
        for (i = 0; i < n; i++) {
          if (!check[i]) {
            ans[j++] = i + 1;
          }
        }
        return ans;
    }
    
    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int n = Integer.parseInt(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("n = " + n + ", k = " + k);
        Mylib ml = new Mylib();

        long start = System.currentTimeMillis();

        int[] result = circularGameLosers(n, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
