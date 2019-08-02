import java.util.*;

public class Solution {
    public int[] gardenNoAdj(int N, int[][] paths) {
        Map<Integer, Set<Integer>> G = new HashMap<>();
        for (int i = 0; i < N; i++) G.put(i, new HashSet<>());
        for (int[] p : paths) {
            G.get(p[0] - 1).add(p[1] - 1);
            G.get(p[1] - 1).add(p[0] - 1);
        }
        int[] res = new int[N];
        for (int i = 0; i < N; i++) {
            int[] colors = new int[5];
            for (int j : G.get(i))
                colors[res[j]] = 1;
            for (int c = 4; c > 0; --c)
                if (colors[c] == 0)
                    res[i] = c;
        }
        return res;
    }

    public void Main(String temp) {
        String str_args = temp.replace("\"", "").replace("]]]", "").trim();
        String[] flds = str_args.split("\\],\\[\\[");
        int N = Integer.parseInt(flds[0].replace("[[", ""));

        Mylib ml = new Mylib();
        String[] data = flds[1].split("\\],\\[");

        int[][] paths = new int[data.length][];
    
        for (int i = 0; i < data.length; i++) {
            paths[i] = ml.str_to_int_array(data[i]);
        }

        System.out.print("paths = [");
        for (int i = 0; i < paths.length; i++) {
            if (i == 0)
                System.out.print("[" + ml.output_int_array(paths[i]) + "]");
            else
                System.out.print(",[" + ml.output_int_array(paths[i]) + "]");
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int[] result = gardenNoAdj(N, paths);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}
