import java.util.*;

public class Solution {
    // 22ms
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<Node> pq = new PriorityQueue<>((a,b) -> a.dis - b.dis);
        for(int i = 0; i < points.length; i++) {
            int dist = points[i][0]*points[i][0] + points[i][1]*points[i][1];
            Node n = new Node(dist, points[i][0], points[i][1]);
            pq.add(n);
        }
        int[][] ans = new int[k][2];
        for (int i = 0; i < k && pq.size() > 0; i++) {
            Node n = pq.poll();
            ans[i][0] = n.x;
            ans[i][1] = n.y;
        }
        return ans;
    }
    
    class Node {
        int dis;
        int x;
        int y;
    
        Node(int dis, int x, int y) {
            this.dis = dis;
            this.x = x;
            this.y = y;
        }
    }
 
    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[[", "").trim().split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] points = ml.stringToIntIntArray(flds[0].split("\\],\\["));
        int k = Integer.parseInt(flds[1].replace("]]", ""));
        System.out.println("points = " + ml.intIntArrayToString(points) + ", k = " + k);

        long start = System.currentTimeMillis();

        int[][] result = kClosest(points, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
