import java.util.*;

public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        // 5ms
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0)
            return false;
        int n = matrix.length, m = matrix[0].length;
        int i = 0, j = m - 1;
        while (i < n && j >= 0) {
            int num = matrix[i][j];
            
            if (num == target)
                return true;
            else if (num > target)
                j--;
            else
                i++;
        }
        return false;
    }

    public String intArrayToString(int[] data) {
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

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String[] flds = temp.trim().split("\\]\\],\\[");

        flds[0] = flds[0].replace("[[[", "");
    //  System.out.println("flds[0] = " + flds[0] + ", flds[0].length = " + Integer.toString(flds[0].length()));

        int[][] matrix;
        if (flds[0].length() > 0) {
            Mylib ml = new Mylib();
            String[] dataStr = flds[0].split("\\],\\[");
        //  System.out.println("dataStr.length = " + Integer.toString(dataStr.length));
            matrix = new int[dataStr.length][];
            System.out.print("matrix = [");
            for (int i = 0; i < dataStr.length; i++) {
                matrix[i] = ml.stringTointArray(dataStr[i]);
                if (i == 0)
                    System.out.println("[" + intArrayToString(matrix[i]) + "]");
                else
                    System.out.println(", [" + intArrayToString(matrix[i]) + "]");
            }
            System.out.println("]");
        } else {
            matrix = new int[0][0];
            System.out.println("matrix = [[]]");
        }

        int target = Integer.parseInt(flds[1].replace("]", ""));
        System.out.println("target = " + Integer.toString(target));

        long start = System.currentTimeMillis();

        boolean result = searchMatrix(matrix, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
