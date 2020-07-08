import java.util.*;

public class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        // 1ms
        Arrays.sort(arr);

        int dif = arr[1] - arr[0];
        for (int i = 2; i < arr.length; i++) {
            if (arr[i] - arr[i - 1] != dif) {
                return false;
            }
        }
        return true;
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringTointArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();
        
        boolean result = canMakeArithmeticProgression(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
