object Solution {
    def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
        var all_nums:Array[Int] = Array.concat(nums1, nums2).sorted
        if (all_nums.length % 2 == 1)
            return all_nums(all_nums.length/2);
        else
            return (all_nums(all_nums.length/2 - 1) + all_nums(all_nums.length/2))/2.0;
    }
}
