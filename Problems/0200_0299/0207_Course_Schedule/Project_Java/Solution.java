import java.util.*;

public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        // 2ms
        ArrayList<Integer>[] G = new ArrayList[numCourses];
        int[] degree = new int[numCourses];
        ArrayList<Integer> bfs = new ArrayList();

        for (int i = 0; i < numCourses; ++i)
            G[i] = new ArrayList<Integer>();

        for (int[] e : prerequisites) {
            G[e[1]].add(e[0]);
            degree[e[0]]++;
        }

        for (int i = 0; i < numCourses; ++i)
            if (degree[i] == 0)
                bfs.add(i);

        for (int i = 0; i < bfs.size(); ++i)
            for (int j: G[bfs.get(i)])
                if (--degree[j] == 0)
                    bfs.add(j);

        return bfs.size() == numCourses;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(", ", ",").trim().split("\\],\\[\\[");
        flds[1] = flds[1].replace("]]]", "");

        int numCourses = Integer.parseInt(flds[0].replace("[", ""));
        Mylib ml = new Mylib();
        int[][] prerequisites;

        if (flds[1].length() > 0) {
            String[] dataStr = flds[1].split("\\],\\[");
            prerequisites = ml.stringToIntIntArray(dataStr);
            System.out.println("prerequisites = " + ml.intIntArrayToString(prerequisites));
        } else {
            prerequisites = new int[0][0];
            System.out.println("prerequisites = [[]]");
        }

        long start = System.currentTimeMillis();

        boolean result = canFinish(numCourses, prerequisites);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
