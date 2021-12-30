import java.util.*;

public class Solution {
    public int[] maxSubsequence(int[] nums, int k) {
        // 5ms
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b)->{
			return b[1] - a[1] != 0 ?  b[1] - a[1] : a[0] - b[0];
        });

        for (int i = 0; i < nums.length; i++) {
            maxHeap.offer(new int[]{i,nums[i]});
        }
		
        PriorityQueue<int[]> answerHeap = new PriorityQueue<>((a,b)->(a[0]-b[0]));
        
        for (int i = k - 1; i >= 0; i--) {
            answerHeap.offer(maxHeap.poll());
        }

        int idx = 0;
        int[] res = new int[k];
        while (!answerHeap.isEmpty()) {
            res[idx] = answerHeap.poll()[1];
            idx++;
        }

        return res;
    }

    public int[] maxSubsequence2(int[] nums, int k) {
        // 8ms
        int n = nums.length;
        int[][] indexAndVal = new int[n][2];

        for (int i = 0; i < n; ++i) {
            indexAndVal[i] = new int[]{i, nums[i]};
        }

        Arrays.sort(indexAndVal, Comparator.comparingInt(a -> -a[1]));
        int[][] maxK = Arrays.copyOf(indexAndVal, k);
        Arrays.sort(maxK, Comparator.comparingInt(a -> a[0]));
        int[] seq = new int[k];

        for (int i = 0; i < k; ++i) {
            seq[i] = maxK[i][1];
        }

        return seq;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int k = Integer.parseInt(flds[1]);
        System.out.println("nums = " + ml.intArrayToString(nums) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int[] result = maxSubsequence(nums, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
