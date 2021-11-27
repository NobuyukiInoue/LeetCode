import java.util.*;

public class Solution {
    public int[] memLeak(int memory1, int memory2) {
        // 3ms
        int i = 0;
        while (true) {
            if (memory1 >= memory2) {
                if (memory1 < i) {
                    break;
                }
                memory1 -= i;
            } else {
                if (memory2 < i) {
                    break;
                }
                memory2 -= i;
            }
            i++;
        }
        return (new int[] {i, memory1, memory2});
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(", ", ",").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        int memory1 = Integer.parseInt(flds[0]);
        int memory2 = Integer.parseInt(flds[1]);
        System.out.println("memory1 = " + memory1 + ", memory2 = " + memory2);

        long start = System.currentTimeMillis();

        int[] result = memLeak(memory1, memory2);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
