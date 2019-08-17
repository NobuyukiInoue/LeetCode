import java.util.*;

public class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        Map<Integer, Integer> count = new HashMap<>();
        int res = 0;
        for (int[] d : dominoes) {
            int k = Math.min(d[0], d[1]) * 10 + Math.max(d[0], d[1]);
            count.put(k, count.getOrDefault(k, 0) + 1);
        }
        for (int v : count.values()) {
            res += v * (v - 1) / 2;
        }
        return res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] dominoes = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            dominoes[i] = ml.str_to_int_array(flds[i]);
        }

        System.out.print("dominoes = [");
        for (int i = 0; i < dominoes.length; i++) {
            if (i == 0)
                System.out.print(ml.output_int_array(dominoes[i]));
            else
                System.out.print("," + ml.output_int_array(dominoes[i]));
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int result = numEquivDominoPairs(dominoes);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
