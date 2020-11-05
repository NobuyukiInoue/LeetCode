import java.util.*;

public class Solution {
    public List<Integer> grayCode(int n) {
        // 32ms
        if (n < 0)
            return new ArrayList<Integer>();
        if (n == 0) {
            List<Integer> list = new ArrayList<Integer>();
            list.add(0);
            return list;
        }

        List<Integer> tmp = grayCode(n - 1);
        List<Integer> result = new ArrayList<Integer>(tmp);
        int addNumber = 1 << (n - 1);

        for (int i = tmp.size() - 1; i >= 0; i--) {
            result.add(addNumber + tmp.get(i));
        }

        return result;
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();
        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        List<Integer> result = grayCode(n);

        long end = System.currentTimeMillis();

        Mylib ml = new Mylib();
        System.out.println("result = " + ml.listIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
