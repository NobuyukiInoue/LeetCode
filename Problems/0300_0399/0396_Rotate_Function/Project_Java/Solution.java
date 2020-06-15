import java.util.*;

public class Solution {
    public int maxRotateFunction(int[] A) {
        // 1ms
        int total = 0, res = 0;
        for (int i = 0; i < A.length; i++) {
            total += A[i];
            res += i * A[i];
        }
        int temp = res;
        for (int i = 0; i < A.length; i++) {
            if (temp - total +A[i]*A.length > res) {
                res = temp - total + A[i]*A.length;
            }
            temp = temp - total + A[i]*A.length;
        }
        return res;
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
        int[] A = ml.stringTointArray(flds);
        System.out.println("A = " + ml.intArrayToString(A));

        long start = System.currentTimeMillis();
        
        int result = maxRotateFunction(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
