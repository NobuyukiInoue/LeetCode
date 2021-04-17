import java.util.*;

public class Solution {
    public int[] addNegabinary(int[] arr1, int[] arr2) {
        // 2ms
        Stack<Integer> s = new Stack<>();
        int i = arr1.length - 1, j = arr2.length - 1, c = 0;
        while (i >= 0 || j >= 0 || c != 0){
            if (i >= 0)
                c += arr1[i--];
            if (j >= 0)
                c += arr2[j--];
            s.push(c & 1);
            c = -(c >> 1);
        }
        while (!s.isEmpty() && s.peek() == 0)
            s.pop();
        int[] res = new int[s.size()];
        i = 0;
        while (!s.isEmpty())
            res[i++] = s.pop();
        return res.length == 0 ? new int[1] : res;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr1 = ml.stringToIntArray(flds[0]);
        int[] arr2 = ml.stringToIntArray(flds[1]);
        System.out.println("arr1 = " + ml.intArrayToString(arr1));
        System.out.println("arr2 = " + ml.intArrayToString(arr2));

        long start = System.currentTimeMillis();

        int[] result = addNegabinary(arr1, arr2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
