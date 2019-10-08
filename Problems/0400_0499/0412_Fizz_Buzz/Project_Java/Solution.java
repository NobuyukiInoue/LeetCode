import java.util.*;

public class Solution {
    public List<String> fizzBuzz(int n) {
        // 1ms
        List<String> results = new ArrayList<String>();
        for (int i = 1; i <= n; ++i) {
            if (i % 3 == 0 && i % 5 == 0) {
                results.add("FizzBuzz");
            } else if (i % 3 == 0) {
                results.add("Fizz");
            } else if (i % 5 == 0) {
                results.add("Buzz");
            } else {
                results.add(Integer.toString(i));
            }
        }

        return results;
    }

    public String List_array_to_String(List<String> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + list.get(0);
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + list.get(i);
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String fld = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(fld);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();
        
        List<String> result = fizzBuzz(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + List_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
