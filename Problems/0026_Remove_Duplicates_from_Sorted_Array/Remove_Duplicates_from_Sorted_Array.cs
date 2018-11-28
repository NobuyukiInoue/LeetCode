using System;

public class Solution {
    public int RemoveDuplicates(int[] nums)
    {
        if (nums.Length == 0)
            return 0;

        int i = 1, n = 1;
        for ( ; i < nums.Length; i++ ) {
               if (nums[i] > nums[i - 1]) {
                   nums[n++] = nums[i];
            }
        }
        
        return n;
    }

    public void Main()
    {
        /*
        int[] temp = new int[] { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
        Console.Write(RemoveDuplicates(temp));
        */
        Console.Write(RemoveDuplicates(new int[] { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 } ));

    }
}
