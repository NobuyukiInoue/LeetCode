import java.util.*;

public class Solution {

    private void NumMatrix_Main(String[] ope, String[] para) {
        if (ope.length != para.length)
            return;
        if (ope.length <= 0 || para.length <= 0)
            return;

        Mylib ml = new Mylib();
        String[] matrix_str = para[0].replace("[[", "").replace("]]", "").split("\\],\\[");
        int[][] matrix = new int[matrix_str.length][];

        for (int n = 0; n < matrix.length; n++) {
            matrix[n] = ml.str_to_int_array(matrix_str[n]);
        }

        NumMatrix nm = new NumMatrix(matrix);

        for (int i = 0; i < ope.length; i++) {
            if (ope[i].equals("NumMatrix")) {
                System.out.println("NumMatrix()");
            } else if (ope[i].equals("sumRegion")) {
                String[] flds = para[i].split(",");
                int row1 = Integer.parseInt(flds[0]);
                int col1 = Integer.parseInt(flds[1]);
                int row2 = Integer.parseInt(flds[2]);
                int col2 = Integer.parseInt(flds[3]);
                int sum = nm.sumRegion(row1, col1, row2, col2);
                System.out.println("sumRegion(" + Integer.toString(row1)
                                  + ", " + Integer.toString(col1)
                                  + ", " + Integer.toString(row2)
                                  + ", " + Integer.toString(col2)
                                  + ") = " + Integer.toString(sum));
            }
        }
    }

    public String output_str_array(String[] words) {
        String result = "[";

        for (int i = 0; i < words.length; i++) {
            if (i == 0) {
                result += "\"" + words[i] + "\"";
            } else {
                result += ",\"" + words[i] + "\"";
            }
        }

        return result + "]";
    }

    public void Main(String arg) {
        String[] flds = arg.replace("\"", "").trim().split("\\],\\[\\[\\[\\[");
        String[] ope = flds[0].replace("\"", "").replace("[", "").replace("]", "").split(",");
        String[] para;
        if (flds.length > 1) {
            String[] params_str1 = flds[1].split("\\]\\]\\],\\[");
            String[] params_str2 = params_str1[1].replace("]]]", "").split("\\],\\[");
            para = new String[1 + params_str2.length];
            para[0] = params_str1[0];
            for (int i = 0; i < params_str2.length; i++) {
                para[i + 1] = params_str2[i].replace("[", "").replace("]", "");
            }
        }
        else {
            para = new String[0];
        }

        System.out.println("ope[] = " + output_str_array(ope));
        System.out.println("para[] = " + output_str_array(para));

        long start = System.currentTimeMillis();
        
        NumMatrix_Main(ope, para);
    
        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
