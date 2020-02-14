import java.util.*;

public class Solution {
    public int[] distributeCandies(int candies, int num_people) {
        int[] res = new int[num_people];
        for (int i = 0; candies > 0; ++i) {
            res[i % num_people] += Math.min(candies, i + 1);
            candies -= i + 1;
        }
        return res;
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

        int candies = Integer.parseInt(flds[0]);
        int num_people = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();
        
        int[] result = distributeCandies(candies, num_people);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Int_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
