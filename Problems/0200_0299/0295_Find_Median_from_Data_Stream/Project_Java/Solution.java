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

    public void Main(String arg) {
        String[] flds = arg.replace("\"", "").trim().split("\\],\\[\\[");
        String[] ope = flds[0].replace("[", "").replace("]", "").split(",");
        String[] params = flds[1].replace("]]]", "").split("\\],\\[");

        Mylib ml = new Mylib();
        System.out.println("ope[] = " + ml.stringArrayToString(ope));
        System.out.println("params[] = " + ml.stringArrayToString(params));

        long start = System.currentTimeMillis();

        MedianFinder_Main(ope, params);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
