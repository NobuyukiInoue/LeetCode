import java.util.*;

class Solution2 {
    // 48ms - 59ms
    int[] arr;
    public Solution2(int[] nums) {
        arr = nums;
    }
    
    public int[] reset() {
        return arr;
    }
    
    public int[] shuffle() {
        Random rand = new Random();
        int[] ans = arr.clone();
        for (int i = 0; i < ans.length; i++) {
            int swp_num = rand.nextInt(ans.length);
            int temp = ans[i];
            ans[i] = ans[swp_num];
            ans[swp_num] = temp;
        }
        return ans;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */
 