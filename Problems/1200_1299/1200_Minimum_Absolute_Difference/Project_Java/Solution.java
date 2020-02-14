import java.util.*;

public class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        List<List<Integer>> results = new ArrayList<List<Integer>>();

        Arrays.sort(arr);
        Integer var_min = 10^7;
        int var_sub = 0;

        for (int i = 0; i < arr.length - 1; ++i) {
            var_sub = arr[i + 1] - arr[i];
            if (var_sub < var_min) {
                var_min = var_sub;
            }
        }

        for (int i = 0; i < arr.length - 1; ++i) {
            var_sub = arr[i + 1] - arr[i];
            if (var_sub == var_min) {
                List<Integer> temp = new ArrayList<Integer>();
                temp.add(arr[i]);
                temp.add(arr[i + 1]);
                results.add(temp);
            }
        }

        return results;
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
        int[] arr = mc.stringTointArray(flds);
        System.out.println("arr = [" + Int_array_to_String(arr) + "]");

        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = minimumAbsDifference(arr);

        long end = System.currentTimeMillis();

        System.out.print("result = [");
        for (int i = 0; i < result.size(); i++) {
            if (i == 0)
                System.out.print(List_array_to_String(result.get(i)));
            else
                System.out.print("," + List_array_to_String(result.get(i)));
        }
        System.out.println("]");

        System.out.println((end - start)  + "ms\n");
    }
}
