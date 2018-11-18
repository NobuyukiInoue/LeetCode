using System;

public class Solution {
    public int SearchInsert(int[] nums, int target)
	{
		int i;
		
		for ( i = 0; i < nums.Length; i++ ) {
			if ( nums[i] < target ) {
				continue;
			}
			else if ( nums[i] >= target ) {
				return i;
			}
		}
		
		return i;
	}

	public void Main()
	{
			Console.Write( SearchInsert(new int[] { 1, 3, 5, 6 }, 5 ) );
	}
}
