import java.util.*;

public class Solution {
    public String categorizeBox(int length, int width, int height, int mass) {
        // 0ms
        boolean bulky = Math.max(length, Math.max(width, height)) >= 1e4 || (long) length*width*height >= 1e9;
        boolean heavy = mass >= 100; 
        if (bulky && heavy)
            return "Both";
        if (bulky)
            return "Bulky";
        if (heavy)
            return "Heavy";
        return "Neither";
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        int length = nums[0], width = nums[1], height = nums[2], mass = nums[3];
        System.out.println("length = " + length + ", widht = " + width + ", height = " + height + ", mass = " + mass);

        long start = System.currentTimeMillis();

        String result = categorizeBox(length, width, height, mass);

        long end = System.currentTimeMillis();

        System.out.println("result = " + result);
        System.out.println((end - start)  + "ms\n");
    }
}
