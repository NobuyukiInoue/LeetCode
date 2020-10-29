import java.util.*;

public class Solution {
    public boolean isValidSerialization(String preorder) {
        // 3ms
        int need = 1;
        for (String val : preorder.split(",")) {
            if (need == 0)
                return false;
            need -= " #".indexOf(val);
        }
        return need == 0;
    }

    public void Main(String temp) {
        String preorder = temp.replace("\"", "").replace(", ", ",").replace("[", "").replace("]", "").trim();
        System.out.println("preorder = " + preorder);

        long start = System.currentTimeMillis();

        Boolean result = isValidSerialization(preorder);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
