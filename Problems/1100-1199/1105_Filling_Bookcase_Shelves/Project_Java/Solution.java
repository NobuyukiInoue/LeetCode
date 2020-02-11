import java.util.*;

public class Solution {
    public int minHeightShelves(int[][] books, int shelf_width) {
        // 0ms
        int[] dp = new int[books.length + 1];
        for (int i = 1; i <= books.length; i++) {
            int width = books[i - 1][0];
            int height = books[i - 1][1];
            dp[i] = dp[i - 1] + height;
            for (int j = i - 1; j > 0; j--) {
                if (width + books[j - 1][0] <= shelf_width) {
                    width += books[j - 1][0];
                    height = Math.max(height, books[j - 1][1]);
                    dp[i] = Math.min(dp[i], dp[j - 1] + height);
                } else {
                    break;
                }
            }
        }

        return dp[books.length];
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace("[[[", "").trim().split("\\]],\\[");

        Mylib ml = new Mylib();

        String[] books_str = flds[0].split("\\],\\[");
        int[][] books = new int[books_str.length][];
    
        for (int i = 0; i < books_str.length; i++) {
            books[i] = ml.stringTointArray(books_str[i]);
        }

        int shelf_width = Integer.parseInt(flds[1].replace("]]", ""));

        System.out.print("books = [");
        for (int i = 0; i < books.length; i++) {
            if (i == 0)
                System.out.print(ml.intArrayToString(books[i]));
            else
                System.out.print("," + ml.intArrayToString(books[i]));
        }
        System.out.println("]");
        System.out.println("shelf_width = " + Integer.toString(shelf_width));

        long start = System.currentTimeMillis();
        
        int result = minHeightShelves(books, shelf_width);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
