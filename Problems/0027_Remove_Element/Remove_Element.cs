using System;

public class Solution {
	public int RemoveElement(int[] nums, int val)
	{
		int i = 0;
		int n = nums.Length;
		while (i < n) {
			if (nums[i] == val) {
				nums[i] = nums[n - 1];
				// reduce array size by one
				n--;
			} else {
				i++;
			}
		}
		return n;
	}

	public void Main()
	{
		Console.Write(RemoveElement(new int[] { 3, 2, 2, 3 }, 2 ));
	}
}