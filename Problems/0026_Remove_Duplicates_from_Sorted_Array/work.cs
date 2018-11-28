using.System;

public class Solution {
    public int RemoveDuplicates(int[] nums) {
        if (nums.Length == 0)
            return 0;
    
        int i = 0, n = 0;
        int[] temp = new int[nums.Length];
        
        temp[0] = nums[0];
        for (i = 1, n = 1; i < nums.Length; i++ ) {
               if (nums[i] > nums[i - 1]) {
                   temp[n++] = nums[i];
            }
        }
        
        return n;
    }

    static public void Main()
    {
            Console.Write(RemoveDuplicates(new int[] = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 } )
    }
}
