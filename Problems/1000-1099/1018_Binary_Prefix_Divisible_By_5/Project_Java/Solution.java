import java.util.*;

public class Solution {
    public List<Boolean> prefixesDivBy5(int[] A) {
        int total = 0;
        List<Boolean> result = new ArrayList<Boolean>();
        for (int i = 0; i < A.length; i++) {
            //total = ((total << 1) + A[i]) % 5;
            total = (total*2 + A[i]) % 5;
            if (total == 0)
                result.add(true);
            else
                result.add(false);
        }
        return result;
    }

    public String List_array_to_String(List<Boolean> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Boolean.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Boolean.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();

        int[] A = ml.str_to_int_array(flds);

        System.out.println("A = " + ml.output_int_array(A));

        long start = System.currentTimeMillis();
        
        List<Boolean> result = prefixesDivBy5(A);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
