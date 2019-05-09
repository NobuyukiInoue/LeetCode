using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization.Json;
using System.Runtime.Serialization;

[DataContract]
public class jsonObject
{
    [DataMember] public bool keyBool = true;
    [DataMember] public int keyInt = 360;
    [DataMember] public double keyDouble = 3.141592653;
    [DataMember] public string keyString = "this is json";
}

public class Solution {

    public void Main(string args)
    {
        string[] filenames = args.Replace("[[","").Replace("]]","").Trim().Split(new string[] {"],["}, StringSplitOptions.None);
        Console.WriteLine("filenames[0] = " + filenames[0]);
        Console.WriteLine("filenames[1] = " + filenames[1]);

        System.Diagnostics.Stopwatch sw = new System.Diagnostics.Stopwatch();
        sw.Start();

        // C#でJSONを読み書きしてみる
        // https://hgotoh.jp/wiki/doku.php/documents/windows/windows-024
        DataContractJsonSerializer js = new DataContractJsonSerializer(typeof(jsonObject));
        //FileStream fs = new FileStream(filenames[0], FileMode.Open);
        FileStream fs = new FileStream("../data1.json", FileMode.Open);
        jsonObject json = (jsonObject)js.ReadObject(fs);
        fs.Close();

        Console.WriteLine(json);

        sw.Stop();
        Console.WriteLine("Execute time ... " + sw.ElapsedMilliseconds.ToString() + "ms\n");
    }
}
