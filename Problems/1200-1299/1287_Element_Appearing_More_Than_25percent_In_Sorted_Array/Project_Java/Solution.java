import java.util.*;

public class Solution {
    public int findSpecialInteger(int[] arr) {
        // 0ms
        int n = arr.length;
        int count = 1;
        int e = arr[0];
        for (int i = 1; i < n; i++) {
            if (arr[i] == e)
                count++;
            else {
                e = arr[i];
                count = 1;
            }
            if(count > n/4)
                return arr[i];
        }
        return arr[0];
    }

    public int findSpecialInteger2(int[] arr) {
        // 5ms
        Map<Integer, Integer> cnt = new HashMap<>();
        int frequency = arr.length / 4;
        for (int a : arr) {
            cnt.put(a, 1 + cnt.getOrDefault(a, 0));
            if (cnt.get(a) > frequency) {
                return a;
            }
        }
        return -1;
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

    public String List_array_to_String(List<Integer> list) {
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

        Mylib mc = new Mylib();
        int[] arr = mc.str_to_int_array(flds);
        System.out.println("arr = [" + Int_array_to_String(arr) + "]");

        long start = System.currentTimeMillis();
        
        int result = findSpecialInteger(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
