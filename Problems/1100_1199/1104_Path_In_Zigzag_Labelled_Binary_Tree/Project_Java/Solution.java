import java.util.*;

public class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        List<Integer> list = new ArrayList<>();
        int level = 0;
        int value = label;
        while (value != 0 ) {
            value = value/2;
            level++;
        }
        while ( level -->= 2 ) {
            list.add(0, label);
            int sum = (int)(Math.pow(2,level) + Math.pow(2, level - 1)) - 1;
            label = sum - label/2;
        }
        list.add(0, 1);
        return list;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int label = Integer.parseInt(fld);
        System.out.println("label = " + Integer.toString(label));

        long start = System.currentTimeMillis();

        List<Integer> result = pathInZigZagTree(label);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
