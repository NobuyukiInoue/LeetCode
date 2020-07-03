import java.util.*;

public class Solution {
    public double average(int[] salary) {
        // 0ms
        double min = salary[0], max = salary[0], sum = 0;
        for (int s : salary) {
            min = Math.min(s, min);
            max = Math.max(s, max);
            sum += s;
        }
        return (sum - min - max) / (salary.length - 2);
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib ml = new Mylib();
        int[] salary = ml.stringTointArray(flds);
        System.out.println("salary = " + ml.intArrayToString(salary));

        long start = System.currentTimeMillis();

        double result = average(salary);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Double.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
