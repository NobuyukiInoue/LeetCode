using System;
using System.Collections.Generic;

public class Solution {
    public int[] TwoSum1(int[] numbers, int target)
    {
        int l = 0, r = numbers.Length - 1;
        int s;
        while (l < r) {
            s = numbers[l] + numbers[r];
            if (s == target)
                return (new int[] {l + 1, r + 1});
            else if (s < target)
                ++l;
            else
                --r;
        }

        return (new int[] {0,0});
    }

    public int[] TwoSum3(int[] numbers, int target)
    {
        for (int i = 0; i < numbers.Length; ++i) {
            int l = i + 1;
            int r = numbers.Length - 1;
            int tmp = target - numbers[i];
            int mid;
            while (l <= r) {
                mid = l + (r - l)/2;
                if (numbers[mid] == tmp)
                    return (new int[] {i+1, mid + 1});
                else if (numbers[mid] < tmp)
                    l = mid + 1;
                else
                    r = mid - 1;
            }
        }

        return (new int[] {0,0});
    }

    public int[] TwoSum_work(int[] numbers, int target)
    {
        int[] resultNumbers = new int [2];
        int i, j;

        for (i = 0; i < numbers.Length; ++i) {
            if (i > 1 && numbers[i] == numbers[i - 1])
                continue;

            resultNumbers[0] = i + 1;

            for (j = i + 1; j < numbers.Length; ++j) {
                if (numbers[i] + numbers[j] == target) {
                    resultNumbers[1] = j + 1;
                    return resultNumbers;
                }
                else {
                    if (numbers[j] == numbers[j - 1])
                        break;
                    if (numbers[i] + numbers[j] > target)
                        break;
                    if (target > 0 && numbers[j] > target)
                        break;
                }
            }
        }

        return resultNumbers;
    }

    private int[] array_str_to_int(string[] workStr)
    {
        int[] numbers = new int[workStr.Length];

        for (int i = 0; i < workStr.Length; i++) {
            numbers[i] = int.Parse(workStr[i]);
        }

        return numbers;
    }

    private string output_array_int(int[] numbers)
    {
        if (numbers.Length == 0)
            return "";

        string resultStr = numbers[0].ToString();
        for (int i = 1; i < numbers.Length; i++)
            resultStr += "," + numbers[i].ToString();

        return resultStr;
    }
	public void Main(string args)
	{
		string[] flds = args.Split(new string[] {", "}, StringSplitOptions.None);
        string[] numbersStr = flds[0].Replace("[","").Replace("]","").Split(',');
        int[] numbers = array_str_to_int(numbersStr);
        int target = int.Parse(flds[1]);

        Console.WriteLine("numbers = [" + output_array_int(numbers) + "], target = " + target);

		System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
		sw.Start();
		
    //  int[] resultNumbers = TwoSum_work(numbers, target);
        int[] resultNumbers = TwoSum1(numbers, target);
    //  int[] resultNumbers = TwoSum3(numbers, target);

		Console.WriteLine("Result = " + output_array_int(resultNumbers));
		
		sw.Stop();
		Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
	}
}
