import java.util.*;

public class Solution {

    private void NumArray_Main(String[] ope, String[] para)
    {
        if (ope.length != para.length)
            return;
        if (ope.length <= 0 || para.length <= 0)
            return;
        
        Mylib ml = new Mylib();
        int[] nums = ml.str_to_int_array(para[0]);

        NumArray nm = new NumArray(nums);

        for (int n = 0; n < ope.length; n++)
        {
            if (ope[n] == "NumArray")
            {
                System.out.println("NumArray()");
            }
            else if (ope[n].equals("update"))
            {
                String[] flds = para[n].split(",");
                int i = Integer.parseInt(flds[0]);
                int val = Integer.parseInt(flds[1]);
                nm.update(i, val);
                System.out.println("update(" + Integer.toString(i)
                                  + ", " + Integer.toString(val)
                                  + ")");
            }
            else if (ope[n].equals("sumRange"))
            {
                String[] flds = para[n].split(",");
                int i = Integer.parseInt(flds[0]);
                int j = Integer.parseInt(flds[1]);
                int sum = nm.sumRange(i, j);
                System.out.println("sumRange(" + Integer.toString(i)
                                  + ", " + Integer.toString(j)
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

    public void Main(String args) {
        String[] flds = args.replace("\"", "").trim().split("\\],\\[\\[\\[");
        String[] ope = flds[0].replace("\"", "").replace("[", "").replace("]", "").split(",");
        String[] para;
        if (flds.length > 1) {
            String[] params_str1 = flds[1].split("\\]\\],\\[");
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
        
        NumArray_Main(ope, para);
    
        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
