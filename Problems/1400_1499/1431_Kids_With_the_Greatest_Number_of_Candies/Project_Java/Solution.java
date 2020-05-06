import java.util.*;
import java.util.stream.Collectors;

public class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // 0ms
        List<Boolean> res = new ArrayList<Boolean>();
        int max = myMax(candies);

        for (int i = 0; i < candies.length; i++) {
            if (candies[i] + extraCandies >= max) {
                res.add(true);
            } else {
                res.add(false);
            }
        }

        return res;
    }

    private int myMax(int[] data) {
        int max = data[0];
        for (int i = 1; i < data.length; i++) {
            if (data[i] > max) {
                max = data[i];
            }
        }

        return max;
    }

    public List<Boolean> kidsWithCandies2(int[] candies, int extraCandies) {
        // 4ms
        int max = Arrays.stream(candies).max().getAsInt();
        return Arrays.stream(candies).mapToObj(candy -> candy + extraCandies >= max).collect(Collectors.toList());
    }

    private String listArrayToString(List<Boolean> data) {
        if (data.size() <= 0)
            return "";

        StringBuilder sb = new StringBuilder("[" + Boolean.toString(data.get(0)));
        for (int i = 1; i < data.size(); i++) {
            sb.append(", " + Boolean.toString(data.get(i)));
        }

        sb.append("]");
        return sb.toString();
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib mc = new Mylib();
        int[] candies = mc.stringTointArray(flds[0]);
        int extraCandies = Integer.parseInt(flds[1]);

        System.out.println("candies = " + mc.intArrayToString(candies));
        System.out.println("extraCandies = " + String.valueOf(extraCandies));

        long start = System.currentTimeMillis();
        
        List<Boolean> result = kidsWithCandies(candies, extraCandies);

        long end = System.currentTimeMillis();

        System.out.println("result = " + listArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
