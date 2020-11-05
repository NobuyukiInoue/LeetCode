import java.util.*;

public class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        // 2ms
        int[] A = new int[triangle.size() + 1];
        for(int i = triangle.size() - 1; i >= 0; i--) {
            for(int j = 0; j < triangle.get(i).size(); j++){
                A[j] = Math.min(A[j], A[j + 1]) + triangle.get(i).get(j);
            }
        }
        return A[0];
    }

    public int minimumTotal2(List<List<Integer>> triangle) {
        // 4ms
        if (triangle.size() <= 0)
            return 0;
        int[][] res = new int[triangle.size()][];
        res[0] = new int[1];
        res[0][0] = triangle.get(0).get(0);
        for (int i = 1; i < res.length; i++) {
            res[i] = new int[triangle.get(i).size()];
            for (int j = 0; j < res[i].length; j++) {
                res[i][j] = 0;
            }
        }

        for (int i = 1; i < triangle.size(); i++) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                if (j == 0)
                    res[i][j] = res[i - 1][j] + triangle.get(i).get(j);
                else if (j == triangle.get(i).size() - 1)
                    res[i][j] = res[i - 1][j - 1] + triangle.get(i).get(j);
                else
                    res[i][j] = Math.min(res[i - 1][j - 1], res[i - 1][j]) + triangle.get(i).get(j);
            }
        }

        return intArrayMin(res[res.length - 1]);
    }

    private int intArrayMin(int[] list) {
        int min = list[0];
        for (int i = 1; i < list.length; i++) {
            if (list[i] < min)
                min = list[i];
        }
        return min;
    }

    public int minimumTotal3(List<List<Integer>> triangle) {
        // 8ms
        if (triangle.size() <= 0)
            return 0;
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(new ArrayList<Integer>(Arrays.asList(triangle.get(0).get(0))));
        for (int i = 1; i < triangle.size(); i++) {
            List<Integer> temp = new ArrayList<Integer>();
            for (int j = 0; j < triangle.get(i).size(); j++) {
                temp.add(0);
            }
            res.add(temp);
        }

        for (int i = 1; i < triangle.size(); i++) {
            for (int j = 0; j < triangle.get(i).size(); j++) {
                if (j == 0)
                    res.get(i).set(j, res.get(i - 1).get(j) + triangle.get(i).get(j));
                else if (j == triangle.get(i).size() - 1)
                    res.get(i).set(j, (res.get(i - 1).get(j - 1) + triangle.get(i).get(j)));
                else
                    res.get(i).set(j, (Math.min(res.get(i - 1).get(j - 1), res.get(i - 1).get(j)) + triangle.get(i).get(j)));
            }
        }

        return listMin(res.get(triangle.size() - 1));
    }

    private int listMin(List<Integer> list) {
        int min = list.get(0);
        for (int i = 1; i < list.size(); i++) {
            if (list.get(i) < min)
                min = list.get(i);
        }
        return min;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        List<List<Integer>> triangle = ml.stringArrayToListListIntArray(flds);
        System.out.println("triangle = " + ml.listListIntArrayToString(triangle));

        long start = System.currentTimeMillis();

        int result = minimumTotal(triangle);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
