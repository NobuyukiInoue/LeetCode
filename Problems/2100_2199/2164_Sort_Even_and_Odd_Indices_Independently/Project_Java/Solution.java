import java.util.*;

public class Solution {
	public int[] sortEvenOdd(int[] nums) {
        // 4ms
		Queue<Integer> even = new PriorityQueue<>();
		Queue<Integer> odd = new PriorityQueue<>(Collections.reverseOrder());
		int i = 0;
		int[] res = new int[nums.length];
		for (int j = 0; j < nums.length; j ++) {
			if (j % 2 == 0) {
				even.offer(nums[j]);
			} else {
				odd.offer(nums[j]);
			}            
		}
		while (!even.isEmpty() && !odd.isEmpty()) {
			res[i] = even.poll();
			i ++;
			res[i] = odd.poll();
			i ++;
		}
		if (!even.isEmpty()) {
			res[i] = even.peek();
		}
		if (!odd.isEmpty()) {
			res[i] = odd.peek();
		}
		return res;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        int[] result = sortEvenOdd(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
