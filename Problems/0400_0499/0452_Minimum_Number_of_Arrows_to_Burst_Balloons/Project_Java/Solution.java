import java.util.*;

public class Solution {
    public int findMinArrowShots(int[][] points) {
        // 14ms
        sortByColumn(points, 1);
        int n = points.length;
        int count = 1;
        int x = points[0][1];
        for (int i = 1; i < n; i++){
            if (x >= points[i][0] && x <= points[i][1]) {
                continue;
            } else {
                count++;
                x = points[i][1];
            }
        }
        return count;
    }

    public static void sortByColumn(int arr[][],int col){
        Arrays.sort(arr, new Comparator<int[]>(){
            @Override
            public int compare(final int[] num1, final int[] num2){
                if (num1[col] > num2[col]){
                    return 1;
                } else {
                    return -1;
                }
            }
        });
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] points = ml.stringToIntIntArray(flds);
        System.out.println("points = " + ml.intIntArrayToString(points));

        long start = System.currentTimeMillis();

        int result = findMinArrowShots(points);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
