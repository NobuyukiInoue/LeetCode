using System;

public class Solution
{
    public string[] FindWords(string[] words)
    {
        if (words.Length <= 0)
            return new string[0];

        string[] words_temp = new string[words.Length];
        for (int i = 0; i < words_temp.Length; ++i)
        {
            words_temp[i] = words[i].ToLower();
        }

        string[] key_row = new string[3];
        key_row[0] = "qwertyuiop";
        key_row[1] = "asdfghjkl";
        key_row[2] = "zxcvbnm";

        bool[] isSame = new bool[words.Length];
        int isSame_Counts = 0;
        int target_row;
        bool first_checked;
        bool isSame_row;

        for (int i = 0; i < words_temp.Length; ++i)
        {
            target_row = -1;
            first_checked = false;
            isSame_row = false;

            if (words_temp[i].Length == 1)
            {
                isSame[i] = true;
                isSame_Counts++;
                continue;
            }

            for (int pos1 = 0; pos1 < words_temp[i].Length; ++pos1)
            {
                if (pos1 == 0)
                    for (int j = 0; j < key_row.Length; ++j)
                    {
                        for (int pos2 = 0; pos2 < key_row[j].Length; ++pos2)
                        {
                            if (words_temp[i][pos1] == key_row[j][pos2])
                            {
                                target_row = j;
                                first_checked = true;
                                break;
                            }
                        }
                        if (first_checked)
                            break;
                    }
                else
                {
                    isSame_row = false;
                    for (int pos2 = 0; pos2 < key_row[target_row].Length; ++pos2)
                        if (words_temp[i][pos1] == key_row[target_row][pos2])
                            isSame_row = true;
                    if (isSame_row == false)
                        break;
                }
            }
            if (isSame_row)
            {
                isSame[i] = true;
                isSame_Counts++;
            }
        }

        string[] results = new string[isSame_Counts];

        for (int i = 0, n = 0; i < words_temp.Length; ++i)
        {
            if (isSame[i])
            {
                results[n++] = words[i];
            }
        }

        return results;
    }

    public string output_str_array(string[] words)
    {
        if (words.Length <= 0)
            return "";
        
        string results = words[0];
        for (int i = 1; i < words.Length; ++i)
        {
            results += ", " + words[i];
        }

        return results;
    }
    public void Main(string args)
    {
        string[] words = args.Replace("\"","").Replace(" ","").Replace("[","").Replace("]","").Trim().Split(',');
        Console.WriteLine("words = " + output_str_array(words));
        
        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        string[] result = FindWords(words);
        Console.WriteLine("result = " + output_str_array(result));
        
        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
