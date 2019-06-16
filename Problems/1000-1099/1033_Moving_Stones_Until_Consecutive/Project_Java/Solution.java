import java.util.*;

public class Solution {
    public int[] numMovesStones(int a, int b, int c) {
        int[] ret = new int[2];
        int[] input = new int[3];

        input[2] = Math.max(Math.max(a, c), b);
        input[0] = Math.min(Math.min(a, c), b);
        input[1] = a + b + c - input[2] - input[0];

        if (input[2] - input[1] == input[1] - input[0] && input[1] - input[0] == 1) {
            ret[0] = 0;
            ret[1] = 0;
            return ret;
        }

        int tmp = input[2] - input[1] > input[1] - input[0]? input[1] - input[0]: input[2] - input[1];

        ret[0] = tmp <= 2? 1: 2;
        ret[1] = input[2] - input[1] - 1 + input[1] - input[0] - 1;

        return ret;
    }

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim().split(",");

        Mylib ml = new Mylib();

        int a = Integer.parseInt(flds[0]);
        int b = Integer.parseInt(flds[1]);
        int c = Integer.parseInt(flds[2]);

        System.out.println("a = " + Integer.toString(a) +
                         ", b = " + Integer.toString(b) +
                         ", c = " + Integer.toString(c));

        long start = System.currentTimeMillis();
        
        int[] result = numMovesStones(a, b, c);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Int_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
