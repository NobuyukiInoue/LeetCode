import java.util.*;

public class Solution {
    public void duplicateZeros(int[] arr) {
        int countZero = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 0) countZero++;
        }
        int len = arr.length + countZero;
        for (int i = arr.length - 1, j = len - 1; i < j; i--, j--) {
            if (arr[i] != 0) {
                if (j < arr.length)
                    arr[j] = arr[i];
            } else {
                if (j < arr.length)
                    arr[j] = arr[i];
                j--;
                if (j < arr.length)
                    arr[j] = arr[i];
            }
        }
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
        int[] arr = new int[flds.length];
        for (int i = 0; i < flds.length; i++) {
            arr[i] = Integer.parseInt(flds[i]);
        }
        System.out.println("arr = " + Int_array_to_String(arr));

        long start = System.currentTimeMillis();
        
        duplicateZeros(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Int_array_to_String(arr));
        System.out.println((end - start)  + "ms\n");
    }
}
