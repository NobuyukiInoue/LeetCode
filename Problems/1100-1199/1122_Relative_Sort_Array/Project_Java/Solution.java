import java.util.*;

public class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int k = 0;
        int[] cnt = new int[1001], ans = new int[arr1.length];
        for (int i : arr1)
            ++cnt[i];
        for (int i : arr2)
            while (cnt[i]-- > 0)
                ans[k++] = i;
        for (int i = 0; i < 1001; ++i)
            while (cnt[i]-- > 0)
                ans[k++] = i;
        return ans;
    }

    public String int_array_to_String(int[] data) {
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
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] arr1 = ml.str_to_int_array(flds[0]);
        int[] arr2 = ml.str_to_int_array(flds[1]);

        System.out.println("arr1 = " + ml.output_int_array(arr1) + ", arr2 = " + ml.output_int_array(arr2));

        long start = System.currentTimeMillis();

        int[] result = relativeSortArray(arr1, arr2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}