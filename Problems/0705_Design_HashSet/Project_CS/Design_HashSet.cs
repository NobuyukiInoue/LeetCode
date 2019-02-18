using System;
using System.Collections.Generic;

public class Solution
{
    private string stringArray2string(string[] words)
    {
        if (words.Length <= 0)
            return "";
        
        string resultStr = "[[" + words[0];
        for (int i = 1; i < words.Length; i++)
        {
            resultStr += "],[" + words[i];
        }

        return resultStr + "]]";
    }

    private void Hash_Main(string[] ope, string[] para)
    {
        if (ope.Length != para.Length)
            return;
        if (ope.Length <= 0 || para.Length <= 0)
            return;

        MyHashSet mh = new MyHashSet();

        for (int i = 0; i < ope.Length; i++)
        {
            // Console.WriteLine("ope[" + i.ToString() + "] = " + ope[i] + ", para[" + i.ToString() + "] = " + para[i]);
            if (ope[i] == "MyHashSet")
            {
                mh = new MyHashSet();
                Console.WriteLine("MyHashSet()");
            }
            else if (ope[i] == "add")
            {
                mh.Add(int.Parse(para[i]));
                Console.WriteLine("Add(" + para[i] + ")");
            }
            else if (ope[i] == "remove")
            {
                mh.Remove(int.Parse(para[i]));
                Console.WriteLine("Remove(" + para[i] + ")");
            }
            else if (ope[i] == "contains")
            {
                bool result = mh.Contains(int.Parse(para[i]));
                Console.WriteLine("Contains(" + para[i] + ") = " + result);
            }
        }
    }

    public void Main(string args)
    {
        string arg_str = args.Replace("\"", "").Replace("[[[","").Replace("]]]","").Trim();
        string[] flds = arg_str.Split(new string[] {"]],[["}, StringSplitOptions.None);
        string[] ope = flds[0].Split(',');
        string[] para = flds[1].Replace("[", "").Replace("]", "").Split(',');

        Console.WriteLine("ope[] = " + stringArray2string(ope));
        Console.WriteLine("para[] = " + stringArray2string(para));

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        Hash_Main(ope, para);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
