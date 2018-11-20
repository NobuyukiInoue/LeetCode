using System;

// Definition for a binary tree node.
public class TreeNode {
	public int val;
	public TreeNode left;
	public TreeNode right;
	public TreeNode(int x) {
		val = x;
	}
}

public class Solution {
	public bool HasPathSum(TreeNode root, int sum) {
		
	}


	public void Main(string args)
	{
	//	Console.WriteLine("args = " + args);
		
		string s = args.Replace("\"", "");
		string[] workStr = s.Split(',');
		Console.WriteLine("data[] = " + output_array_int(prices));

		System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
		sw.Start();

		Console.WriteLine("Result = " + MaxProfit(prices).ToString());
		
		sw.Stop();
		Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
	}
}
