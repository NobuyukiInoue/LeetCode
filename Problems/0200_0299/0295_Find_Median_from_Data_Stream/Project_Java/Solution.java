import java.util.*;

public class Solution {

    private void MedianFinder_Main(String[] ope, String[] params) {
        if (ope.length != params.length)
            return;
        if (ope.length <= 0 || params.length <= 0)
            return;

        MedianFinder mf = new MedianFinder();

        for (int i = 0; i < ope.length; i++) {
            if (ope[i].equals("MedianFinder")) {
                System.out.println("MedianFinder()");

            } else if (ope[i].equals("addNew")) {
                mf.addNum(Integer.parseInt(params[i]));
                System.out.println("addNew(" +  params[i] + ")");

            } else if (ope[i].equals("medianFinder")) {
                double res = mf.findMedian();
                System.out.println("medianFinder(" +  params[i] + ") ... " + Double.toString(res));

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
        String[] flds = arg.replace("\"", "").trim().split("\\],\\[\\[");
        String[] ope = flds[0].replace("[", "").replace("]", "").split(",");
        String[] params = flds[1].replace("]]]", "").split("\\],\\[");

        System.out.println("ope[] = " + output_str_array(ope));
        System.out.println("params[] = " + output_str_array(params));

        long start = System.currentTimeMillis();
        
        MedianFinder_Main(ope, params);
    
        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
