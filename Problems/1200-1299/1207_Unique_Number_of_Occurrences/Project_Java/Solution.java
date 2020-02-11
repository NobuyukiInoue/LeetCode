import java.util.*;

public class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> d = new HashMap<>();
        for (int a: arr)
            d.put(a, d.getOrDefault(a, 0) + 1);
        return d.size() == new HashSet<>(d.values()).size();
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
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] arr = mc.stringTointArray(flds);
        System.out.println("arr = [" + Int_array_to_String(arr) + "]");

        long start = System.currentTimeMillis();
        
        Boolean result = uniqueOccurrences(arr);

        long end = System.currentTimeMillis();
        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
