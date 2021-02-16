import java.util.*;

public class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        // 40ms
        Map<Integer, Integer> dic = new HashMap<>();
        int maxCount = 0;
        for (int i = lowLimit; i <= highLimit; i++){
            int num = i;
            int digits = 0;
            while (num > 0) {
                digits += num%10;
                num /= 10;
            }
            dic.put(digits, dic.getOrDefault(digits, 0) + 1);
            if (dic.get(digits) > maxCount) {
                maxCount = dic.get(digits);
            }
        }
        return maxCount;
    }

    public int countBalls2(int lowLimit, int highLimit) {
        // 41ms
        Map<Integer, Integer> dic = new HashMap<>();
        int maxCount = 0;
        for(int i = lowLimit ; i <= highLimit; i++){
            int num = i;
            int digits = 0;
            while (num > 0){
                digits += num %10;
                num /= 10;
            }
            dic.put(digits, dic.getOrDefault(digits, 0) + 1);
            maxCount = Math.max(maxCount, dic.get(digits));
        }
        return maxCount;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("[[", "").replace("]]", "").replace(", ", ",").trim().split("\\],\\[");
        int lowLimit = Integer.parseInt(flds[0]);
        int highLimit = Integer.parseInt(flds[1]);

        long start = System.currentTimeMillis();

        int result = countBalls(lowLimit, highLimit);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
