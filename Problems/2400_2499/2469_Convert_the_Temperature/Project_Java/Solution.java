import java.util.*;

public class Solution {
    public double[] convertTemperature(double celsius) {
        // 0ms
        return new double[] {celsius + 273.15, celsius * 1.80 + 32.00};
    }

    public String dblArrayToString(double[] nums) {
        if (nums == null)
            return "[]";
        if (nums.length <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Double.toString(nums[0]));
        for (int i = 1; i < nums.length; ++i)
            resultStr.append("," + Double.toString(nums[i]));
        resultStr.append("]");

        return resultStr.toString();
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        double celsius = Double.parseDouble(flds);
        System.out.println("n = " + Double.toString(celsius));

        long start = System.currentTimeMillis();

        double[] result = convertTemperature(celsius);

        long end = System.currentTimeMillis();

        System.out.println("result = " + dblArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
