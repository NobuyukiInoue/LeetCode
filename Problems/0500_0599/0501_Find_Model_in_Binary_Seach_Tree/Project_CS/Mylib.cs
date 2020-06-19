public class Mylib
{
    public int[] StringToIntArray(string s)
    {
        if (s.Length <= 0)
            return null;

        string[] flds = s.Split(",");
        int[] nums = new int[flds.Length];

        if (flds.Length <= 0)
            return nums;

        for (int i = 0; i < nums.Length; ++i) {
            nums[i] = int.Parse(flds[i]);
        }

        return nums;
    }

    public string IntArrayToString(int[] nums)
    {
        if (nums.Length <= 0)
            return "";

        string resultStr = nums[0].ToString();

        for (int i = 1; i < resultStr.Length; ++i)
        {
            resultStr += ", " + nums[i].ToString();
        }

        return resultStr;
    }
}
