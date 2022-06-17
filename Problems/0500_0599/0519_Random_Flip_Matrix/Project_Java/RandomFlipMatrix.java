import java.util.*;

class RandomFlipMatrix {
    // 23ms - 52ms
    private int rows;
    private int cols;
    private int limit;
    private Random rand;
    private HashMap<Integer, Integer> used;

    public RandomFlipMatrix(int m, int n) {
        rows = m;
        cols = n;
        limit = m*n;
        rand = new Random();
        used = new HashMap<>();
    }
    
    public int[] flip() {
        int r = rand.nextInt(limit--);
        int x = used.getOrDefault(r, r);
        used.put(r, used.getOrDefault(limit, limit));
        return new int[]{x / cols, x % cols};
    }
    
    public void reset() {
        used.clear();
        limit = rows*cols;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(m, n);
 * int[] param_1 = obj.flip();
 * obj.reset();
 */
