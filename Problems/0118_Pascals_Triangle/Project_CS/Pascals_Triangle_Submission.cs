using System;
using System.Collections.Generic;

public class Solution2 {
    public IList<IList<int>> Generate(int numRows)
    {
           IList<int> list = new List<int>();
        IList<IList<int>> list2 = new List<IList<int>>();

        for (int i = 0; i < numRows ; i++) {
            for (int j = 0; j < i + 1; j++) {
                int sum = numsum2(i, j);
                if (sum != 0) {
                    list.Add(sum);
                }
            }
            list2.Add(list.ToArray());
            list.Clear();
        }
        return list2;
    }
    
    static int numsum2(int number, int number2)
    {
        double sum = 1;
        int number3 = number - number2;
        while (number > 0 && number2 > 0 && number3 > 0) {
            sum = sum * number / number2 / number3;
            number--;
            if (number2 > 1) {
                number2--;
            }
            if (number3 > 1) {
                number3--;
            }
        }
        return Convert.ToInt32(sum);
    }

    private int[] calc_next(int[] data)
    {
        int[] result = new int[data.Length + 1];

        result[0] = 1;
        result[result.Length - 1] = 1;

        int i;
        for(i = 1; i < result.Length / 2; ++i) {
            if ( i - 1 >= 0) {
                result[i] = data[i - 1] + data[i];
                result[result.Length - 1 - i] = data[data.Length - 1 - i + 1] + data[data.Length - 1 - i];
            }
        }

        if (result.Length % 2 == 1)
            result[i] =  data[i - 1] + data[i];

        return result;
    }

    private void test_Main()
    {
        calc_next(new int[] {1});
        calc_next(new int[] {1,1});
        calc_next(new int[] {1,2,1});
        calc_next(new int[] {1,3,3,1});
        calc_next(new int[] {1,4,6,4,1});
    }

    private void test2_Main(int num)
    {
        int[] current_data = new int[] {1};
        int[] next_data;
        for (int i = 0; i <= num; ++i) {
            next_data = calc_next(current_data);
            Console.WriteLine("result[" + i.ToString() + "] = " + output_array(next_data));
            current_data = next_data;
        }
    }

    private string output_array(int[] data)
    {
        if (data.Length == 0)
            return "";

        string result = data[0].ToString();
        for (int i = 1; i < data.Length; ++i)
            result += "," + data[i].ToString();

        return result;
    }

    public void Main(string args)
    {
        Console.WriteLine("args = " + args);
        int num = int.Parse(args);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

    //    Ilist<List<int>> results_array = new IList(num);

    //    test_Main();
        test2_Main(10);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms");
    }
}
