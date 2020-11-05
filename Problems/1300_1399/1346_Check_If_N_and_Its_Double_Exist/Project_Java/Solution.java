import java.util.*;

public class Solution {
    public boolean checkIfExist(int[] arr) {
        // 1ms
        HashSet<Integer> lst = new HashSet<Integer>();
        for (int num : arr) {
            if (lst.contains(num*2) || num%2 == 0 && lst.contains(num/2))
                return true;
            lst.add(num);
        }
        return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] arr = ml.stringToIntArray(flds);
        System.out.println("arr = " + ml.intArrayToString(arr));

        long start = System.currentTimeMillis();
        
        boolean result = checkIfExist(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
