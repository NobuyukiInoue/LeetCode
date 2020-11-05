import java.util.*;

public class Solution {
    public int firstBadVersion(int n) {
        int left = 1, right = n, mid;
        while(left < right) {
            mid = (left & right) + ((left ^ right) >> 1);
            if (isBadVersion(mid))
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }

    public Boolean isBadVersion(int n) {
        if (n >= 4)
            return true;
        else
            return false;
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = firstBadVersion(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
