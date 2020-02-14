import java.util.*;

public class Solution {
    public int twoCitySchedCost(int[][] costs) {
        if (costs.length == 0 || costs[0].length == 0) {
            return 0;
        }
        int[] diff = new int[costs.length];
        int sum = 0;

        for (int i = 0; i < diff.length; i++) {
            sum += costs[i][0];
            diff[i] = costs[i][1] - costs[i][0];
        }
        Arrays.sort(diff);

        for (int i = 0; i < diff.length/2; i++) {
            sum += diff[i];
        }
        return sum;
    }

    public int twoCitySchedCost2(int[][] costs) {
        Arrays.sort(costs, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return (a[1] - a[0]) - (b[1] - b[0]);
            }
        });
        int cost = 0;
        for (int i = 0; i < costs.length / 2; i++) {
            cost += costs[i][1] + costs[costs.length-i-1][0];
        }
        return cost;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();

        int[][] costs = new int[flds.length][];
    
        for (int i = 0; i < flds.length; i++) {
            costs[i] = ml.stringTointArray(flds[i]);
        }

        System.out.print("costs = [");
        for (int i = 0; i < costs.length; i++) {
            if (i == 0)
                System.out.print("[" + ml.intArrayToString(costs[i]) + "]");
            else
                System.out.print(",[" + ml.intArrayToString(costs[i]) + "]");
        }
        System.out.println("]");

        long start = System.currentTimeMillis();
        
        int result = twoCitySchedCost(costs);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
