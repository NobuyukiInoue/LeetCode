using System;

public class Solution
{
	public int MaxProfit(int[] prices) {
		int max = 0;
		int sum_max = 0;
		int min = int.MaxValue;

		for(int i = 0; i < prices.Length; i++)
		{
			if(min > prices[i])
				min = prices[i];
			if(prices[i] - min > max)
				max = prices[i] - min;
			if(prices[i] - min > 0) {
				sum_max += prices[i] - min;
				min = prices[i];
			}
		}
		
		if (max > sum_max)
			return max;
		else
			return sum_max;
	}

	public int[] array_str_to_int(string[] workStr)
	{
		int[] resultArray = new int[workStr.Length];
		
		for (int i = 0; i < workStr.Length; ++i) {
			resultArray[i] = int.Parse(workStr[i]);
		}
		
		return resultArray;
	}
	
	public string output_array_int(int[] data)
	{
		string resultStr = data[0].ToString();
		for (int i = 1; i < data.Length; ++i) {
			resultStr += "," + data[i].ToString();
		}
		
		return resultStr;
	}

	public void Main(string args)
	{
	//	Console.WriteLine("args = " + args);
		
		string s = args.Replace("\"", "");
		string[] workStr = s.Split(',');
		int[] prices = array_str_to_int(workStr);
		Console.WriteLine("data[] = " + output_array_int(prices));

		System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
		sw.Start();

		Console.WriteLine("Result = " + MaxProfit(prices).ToString());
		
		sw.Stop();
		Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
	}
}
