import java.util.*;

public class Solution {
    public int nextGreaterElement(int n) {
        // 0ms
        int[] s = getDigitsArray(n);
        int i = s.length - 1;
        while (i - 1 >= 0 && s[i] <= s[i - 1]) {
            i--;
        }
        if (i == 0) {
            return -1;
        }
        int j = i;
        while (j + 1 < s.length && s[j + 1] > s[i - 1]) {
            j++;
        }

        swap(s, i - 1, j);
        reversed(s, i);

        long ans = 0;
        for (i = 0; i < s.length; i++) {
            ans *= 10;
            ans += s[i];
        }
        if (ans <=((1<<31) - 1))
            return (int)ans;
        return -1;
    }

    private int[] getDigitsArray(int n) {
        List<Integer> s = new ArrayList<>();
        int temp_n = n;
        while (temp_n > 0) {
            s.add(temp_n % 10);
            temp_n /= 10;
        }
        int[] res = new int[s.size()];
        for (int i = 0; i < res.length; i++) {
            res[i] = s.get(res.length - i - 1);
        }
        return res;
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }

    private void reversed(int[] nums, int start_pos) {
        for (int k = start_pos; k < nums.length - (nums.length - start_pos)/2; k++) {
            swap(nums, k, nums.length + start_pos - k - 1);
        }
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        int n = Integer.parseInt(flds);
        System.out.println("n = " + Integer.toString(n));

        long start = System.currentTimeMillis();

        int result = nextGreaterElement(n);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Integer.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
