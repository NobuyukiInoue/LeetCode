import java.util.*;

public class Solution {
    public void Main(String temp) {
        String flds_str = temp.replace(", ", ",").trim();

        Mylib ml = new Mylib();
        OperateNestedInteger oni = new OperateNestedInteger();
        List<NestedInteger> flds = oni.createListNestedInteger(flds_str);
        System.out.println("flds = " + oni.listNestedIntegerToString(flds));

        long start = System.currentTimeMillis();

        List<Integer> result = oni.getNestedIterator(flds);

        long end = System.currentTimeMillis();
 
        System.out.println("result = " + ml.listIntArrayToString(result));

        System.out.println((end - start)  + "ms\n");
    }
}
