public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int sum = 0, count = 0;

        int[] all_nums = nums1.Concat(nums2).ToArray();
        
        for (int i = 0; i < all_nums.Length - 1; i++) {
            for (int j = i + 1; j < all_nums.Length; j++) {
                if (all_nums[i] > all_nums[j]) {
                    int temp = all_nums[i];
                    all_nums[i] = all_nums[j];
                    all_nums[j] = temp;
                }
            }
        }
        
        if (all_nums.Length % 2 == 1){
            return(all_nums[all_nums.Length / 2]);
        }
        else{
            return((double)(all_nums[all_nums.Length/2 - 1] + all_nums[all_nums.Length/2])/ 2);
        }
        
        /*
        8   012 34 567
        9   0123 4 5678
        */
    }
}

