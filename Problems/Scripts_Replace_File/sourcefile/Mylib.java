import java.util.*;

public class Mylib {
    public int[] stringToIntArray(String s) {
        if (s.length() <= 0)
            return null;

        String[] flds = s.split(",");
        int[] nums = new int[flds.length];

        if (flds.length <= 0)
            return nums;

        for (int i = 0; i < nums.length; ++i) {
            nums[i] = Integer.parseInt(flds[i]);
        }

        return nums;
    }

    public String intArrayToString(int[] nums) {
        if (nums == null)
            return "[]";
        if (nums.length <= 0)
            return "[]";

        StringBuilder resultStr = new StringBuilder("[" + Integer.toString(nums[0]));
        for (int i = 1; i < nums.length; ++i)
            resultStr.append("," + Integer.toString(nums[i]));
        resultStr.append("]");

        return resultStr.toString();
    }

    private String stringArrayToString(String[] flds) {
        if (flds.length <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[\"" + flds[0] + "\"");
        for (int i = 1; i < flds.length; i++)
            sb.append(", \"" + flds[i] + "\"");
        sb.append("]");

        return sb.toString();
    }

    public String listArrayToString(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + Integer.toString(list.get(i)));
        }
        sb.append("]");

        return sb.toString();
    }

    public String listListArrayToString(List<List<Integer>> list) {
        if (list.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + listArrayToString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + listArrayToString(list.get(i)));
        }
        sb.append("]");

        return sb.toString();
    }
}
