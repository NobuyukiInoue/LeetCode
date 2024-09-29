import java.util.*;

public class Solution {
    public int[][] diagonalSort(int[][] mat) {
        // 3ms
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        for (int i = mat.length - 1 ; i >= 0; i--){
            recurseDiag(mat, i, 0, pq);
            insertDiag(mat, i, 0, pq);
        }
        for (int j = 1; j < mat[0].length; j++){
            recurseDiag(mat, 0, j, pq);
            insertDiag(mat, 0, j, pq);
        }
        return mat;
    }

    public void recurseDiag(int[][] mat, int i, int j, PriorityQueue<Integer> pq){
        pq.offer(mat[i][j]);
        while (i + 1 >= 0 && i + 1 < mat.length && j + 1 >= 0 && j + 1 < mat[0].length){
            i = i + 1;
            j = j + 1;
            pq.offer(mat[i][j]);
        }
    }

    public void insertDiag(int[][] mat, int i, int j, PriorityQueue<Integer> pq){
        mat[i][j] = pq.poll();
        while (i + 1 >= 0 && i + 1 < mat.length && j + 1 >= 0 && j + 1 < mat[0].length){
            i = i + 1;
            j = j + 1;
            mat[i][j] = pq.poll();
        }
    }

    public int[][] diagonalSor_byPQ(int[][] mat) {
        // 11ms
        int m = mat.length, n = mat[0].length;
        HashMap<Integer, PriorityQueue<Integer>> d = new HashMap<>();
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                d.putIfAbsent(i - j, new PriorityQueue<>());
                d.get(i - j).add(mat[i][j]);
            }
        }
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
            mat[i][j] = d.get(i - j).poll();
        return mat;
    }

    public int[][] diagonalSort_byLinkedList(int[][] mat) {
        // 20ms
        HashMap<Integer, LinkedList<Integer>> d = new HashMap<>();
        int m = mat.length, n = mat[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (d.containsKey(i - j)) {
                    LinkedList<Integer> temp = new LinkedList<>(d.get(i - j));
                    temp.add(mat[i][j]);
                    d.replace(i - j, temp);
                } else {
                    d.put(i - j, new LinkedList<>(Arrays.asList(mat[i][j])));
                }
            }
        }
        for (int k : d.keySet()) {
            Collections.sort(d.get(k));
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                mat[i][j] = d.get(i - j).remove(0);
            }
        }
        return mat;
    }

    public int[][] diagonalSort_byArrayList(int[][] mat) {
        // 16ms - 17ms
        HashMap<Integer, List<Integer>> d = new HashMap<>();
        int m = mat.length, n = mat[0].length;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (d.containsKey(i - j)) {
                    List<Integer> temp = new ArrayList<>(d.get(i - j));
                    temp.add(mat[i][j]);
                    d.replace(i - j, temp);
                } else {
                    d.put(i - j, new ArrayList<>(Arrays.asList(mat[i][j])));
                }
            }
        }
        for (int k : d.keySet()) {
            Collections.sort(d.get(k));
        };
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                mat[i][j] = d.get(i - j).remove(0);
            }
        }
        return mat;
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();

        Mylib ml = new Mylib();
        int[][] mat = ml.stringToIntIntArray(flds.split("\\],\\["));
        System.out.println("mat = " + ml.intIntArrayToString(mat));

        long start = System.currentTimeMillis();

        int[][] result = diagonalSort(mat);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
