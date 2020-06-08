import java.util.*;
import java.util.List;

public class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        // 3ms
        int [] res = new int[numCourses];
        List<Integer> order = new ArrayList<>();
        List[] parents = new List[numCourses];
        for (int i = 0; i < numCourses; i++) {
            parents[i] = new ArrayList<Integer>();
        }
        for (int[] prereq: prerequisites) {
            parents[prereq[0]].add(prereq[1]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!genOrder(numCourses, parents, i, order, new boolean[numCourses] )) {
                return new int[0]; 
            }
        }
        for (int i = 0; i < numCourses; i++) {
            res[i] = order.get(i);
        }
        return res;
    }
    public boolean genOrder(int n, List[] parents, int i, List<Integer> order, boolean[] visited) {
        if (parents[i] == null) {
            return true;
        }
        if (visited[i]) {
            return false; 
        }
        visited[i] = true;
        if (parents[i] == null) return true;
        List<Integer> myParents = parents[i];
        for (int paren: myParents) {
            if (!genOrder(n, parents, paren, order, visited))
                return false;
        }
        visited[i] = false;
        order.add(i);
        parents[i] = null;

        return true;
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String[] flds;

        if (temp.indexOf("],[[") >= 0) {
            flds = temp.replace(", ", ",").trim().split("\\],\\[\\[");
            flds[1] = flds[1].replace("]]]", "");
        } else {
            flds = temp.replace(", ", ",").trim().split("\\],\\[");
            flds[1] = flds[1].replace("]]", "");
        }

        int numCourses = Integer.parseInt(flds[0].replace("[", ""));
        Mylib ml = new Mylib();
        int[][] prerequisites;

        if (flds[1].length() > 0) {
            String[] dataStr = flds[1].split("\\],\\[");
            prerequisites = new int[dataStr.length][];
            System.out.print("prerequisites = [");
            for (int i = 0; i < dataStr.length; i++) {
                prerequisites[i] = ml.stringTointArray(dataStr[i]);
                if (i == 0)
                    System.out.println("[" + ml.intArrayToString(prerequisites[i]) + "]");
                else
                    System.out.println(", [" + ml.intArrayToString(prerequisites[i]) + "]");
            }
            System.out.println("]");
        } else {
            prerequisites = new int[0][0];
            System.out.println("prerequisites = []");
        }

        long start = System.currentTimeMillis();

        int[] result = findOrder(numCourses, prerequisites);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
