using System;
using System.Collections.Generic;

public class Solution {
    public IList<string> ReadBinaryWatch(int num)
    {
        var result = new List<string>();

        var hourNumbers   = new int[] { 8,   4, 2, 1 };
        var minuteNumbers = new int[] { 32, 16, 8, 4, 2, 1 };

        for (int i = 0; i <= num; i++)
        {
            var listHours   = generateDigits(hourNumbers, i);
            var listMinutes = generateDigits(minuteNumbers, num - i);

            foreach (var hours in listHours)
            {
                if (hours >= 12)
                {
                    continue; 
                }

                foreach (var minutes in listMinutes)
                {
                    if (minutes >= 60)
                    {
                        continue; 
                    }

                    var minuteTwoDigits = minutes.ToString();
                    var minutesText = minutes < 10 ? "0" + minuteTwoDigits : minuteTwoDigits;

                    result.Add(hours + ":" + minutesText); 
                }
            }
        }

        return result; 
    }

    private static List<int> generateDigits(int[] numbers, int count)
    {
        var result = new List<int>();

        generateDigitsBySteps(numbers, count, 0, 0, result);

        return result; 
    }

    /// <summary>
    /// count how many ways to construct the digits:
    /// 
    /// </summary>
    /// <param name="numbers"></param>
    /// <param name="count"></param>
    /// <param name="start"></param>
    /// <param name="sum"></param>
    /// <param name="result"></param>
    private static void generateDigitsBySteps(int[] numbers, int count, int start, int sum, List<int> result)
    {
        if (count == 0)
        {
            result.Add(sum); 
        }

        for (int i = start; i < numbers.Length; i++)
        {
            generateDigitsBySteps(numbers, count - 1, i + 1, sum + numbers[i], result); 
        }
    } 

    public string Output_IList(IList<string> arr)
    {
        if (arr.Count < 1)
            return "";

        string resultStr = arr[0];
        for (int i = 0; i < arr.Count; ++i)
            resultStr += ", " + arr[i];
        
        return resultStr;
    }

    public void Main(string args)
    {
        int num = int.Parse(args);

        Console.WriteLine("num = " + num.ToString());

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();
        
        IList<string> result = ReadBinaryWatch(num);

        Console.WriteLine("result = " + Output_IList(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
