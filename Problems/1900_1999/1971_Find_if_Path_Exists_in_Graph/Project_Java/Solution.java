import java.util.*;
import java.util.stream.*;

class DisjointSetUnion{
    private int[] parent;
    private int N;
    
    public DisjointSetUnion(int n){
        this.N = n;
        this.parent = new int[this.N];
        for(int i = 0; i < this.N; i++){
            this.parent[i] = i;
        }
    }
    
    public boolean areConnected(int u, int v){
        return find(u) == find(v);
    }
    
    public void union(int u, int v){
        if(u != v){
            int a = find(u);
            int b = find(v);
            parent[a] = b;
        }
    }
    
    private int find(int u){
        int x = u;
        while(x != this.parent[x]){
            x = this.parent[x];
        }
        
        this.parent[u] = x;
        return x;
    }
}

class Solution {
    public boolean validPath(int n, int[][] edges, int start, int end) {
        // 9ms
        DisjointSetUnion set = new DisjointSetUnion(n);
        for(int[] edge : edges){
            set.union(edge[0], edge[1]);
        }
        
        return set.areConnected(start, end);
    }

/*
public class Solution {
    public boolean validPath(int n, int[][] edges, int start, int end) {
        return true;
    }

    public boolean validPath1(int n, int[][] edges, int start, int end) {
        // 146ms
        Map<Integer, List<Integer>> g = new HashMap<>();
        IntStream.range(0, n).forEach(u -> g.put(u, new ArrayList<>()));
        for (int[] e : edges) {
            g.get(e[0]).add(e[1]);
            g.get(e[1]).add(e[0]);
        }
        Set<Integer> seen = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        for (q.add(start), seen.add(start); !q.isEmpty(); )
            if (q.peek() == end)
                return true;
            else g.get(q.poll()).stream().filter(seen::add).forEach(q::offer);
        return false;
    }

    public boolean validPath2(int n, int[][] edges, int start, int end) {
        // 120ms
        Map<Integer, List<Integer>> g = new HashMap<>();
        IntStream.range(0, n).forEach(u -> g.put(u, new LinkedList<>()));
        Arrays.stream(edges).forEach(e -> {g.get(e[0]).add(e[1]); g.get(e[1]).add(e[0]);});
        Set<Integer> seen = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        for (q.add(start), seen.add(start); !q.isEmpty() && q.peek() != end; )
            g.get(q.poll()).stream().filter(seen::add).forEach(q::offer);
        return !q.isEmpty();
    }
*/

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").trim().split("\\],\\[\\[");
        int n = Integer.parseInt(flds[0].replace("[", ""));
        String[] flds1 = flds[1].split("\\]\\],\\[");

        Mylib ml = new Mylib();
        int[][] edges;
        if (flds1[0].length() == 0) {
            edges = new int[][]{};
        } else {
            edges = ml.stringToIntIntArray(flds1[0].split("\\],\\["));
        }
        String[] flds2 = flds1[1].replace("]]", "").split("\\],\\[");
        int v_start = Integer.parseInt(flds2[0]);
        int v_end = Integer.parseInt(flds2[1]);
        System.out.println("n = " + Integer.toString(n) + ", edges = " + ml.intIntArrayToString(edges) + ", start = " + Integer.toString(v_start) + ", end = " + Integer.toString(v_end));

        long start = System.currentTimeMillis();

        boolean result = validPath(n, edges, v_start, v_end);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
