import java.util.*;

public class Mylib {
    public int[] stringToIntArray(String s) {
        if (s == null)
            return null;
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

    public int[][] stringToIntIntArray(String[] s) {
        if (s == null)
            return null;

        int[][] nums = new int[s.length][];
        for (int i = 0; i < s.length; i++) {
            nums[i] = stringToIntArray(s[i]);
        }

        return nums;
    }

    public String[] stringToStringArray(String s) {
        if (s == null)
            return null;
        if (s.length() <= 0)
            return null;

        String[] flds = s.split(",");
        String[] words = new String[flds.length];

        if (flds.length <= 0)
            return words;

        for (int i = 0; i < words.length; ++i) {
            words[i] = flds[i];
        }

        return words;
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

    public String intIntArrayToString(int[][] nums) {
        if (nums == null)
            return "[]";

        if (nums.length <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + intArrayToString(nums[0]));
        for (int i = 1; i < nums.length; i++) {
            sb.append("," + intArrayToString(nums[i]));
        }
        sb.append("]");

        return sb.toString();
    }

    public String matrixToString(int[][] list) {
        if (list == null)
            return "[]";

        Mylib ml = new Mylib();
        StringBuilder sb = new StringBuilder("[\n  " + intArrayToString(list[0]) + "\n");
        for (int i = 1; i < list.length; i++) {
            sb.append(" ," + intArrayToString(list[i]) + "\n") ;
        }

        sb.append("]");
        return sb.toString();
    }

    public String stringArrayToString(String[] flds) {
        if (flds == null)
            return "[]";

        StringBuilder sb = new StringBuilder("[\"" + flds[0] + "\"");
        for (int i = 1; i < flds.length; i++)
            sb.append(", \"" + flds[i] + "\"");
        sb.append("]");

        return sb.toString();
    }

    public String listIntArrayToString(List<Integer> list) {
        if (list == null)
            return "";
        if (list.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + Integer.toString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + Integer.toString(list.get(i)));
        }
        sb.append("]");

        return sb.toString();
    }

    public String listListIntArrayToString(List<List<Integer>> list) {
        if (list == null)
            return "";
        if (list.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[" + listIntArrayToString(list.get(0)));
        for (int i = 1; i < list.size(); i++) {
            sb.append("," + listIntArrayToString(list.get(i)));
        }
        sb.append("]");

        return sb.toString();
    }


    public List<Integer> stringToListIntArray(String s) {
        List<Integer> nums = new ArrayList<Integer>();

        if (s == null)
            return nums;
        if (s.length() <= 0)
            return nums;

        String[] flds = s.split(",");

        if (flds.length <= 0)
            return nums;

        nums.add(Integer.parseInt(flds[0]));
        for (int i = 1; i < flds.length; ++i) {
            nums.add(Integer.parseInt(flds[i]));
        }

        return nums;
    }

    public List<List<Integer>> stringArrayToListListIntArray(String[] s)
    {
        List<List<Integer>> list = new ArrayList<List<Integer>>();

        if (s == null)
            return list;
        if (s.length <= 0)
            return list;

        for (int i = 0; i < s.length; i++) {
            list.add(stringToListIntArray(s[i]));
        }

        return list;
    }

    public String listStringArrayToString(List<String> flds) {
        if (flds == null)
            return "";
        if (flds.size() <= 0)
            return "";

        StringBuilder sb = new StringBuilder();
        sb.append("[" + flds.get(0));
        for (int i = 1; i < flds.size(); i++)
            sb.append(", " + flds.get(i));

        return sb.append("]").toString();
    }

    public String listListStringArrayToString(List<List<String>> flds) {
        if (flds == null)
            return "";
        if (flds.size() <= 0)
            return "";

        StringBuilder sb = new StringBuilder();
        sb.append("[" + listStringArrayToString(flds.get(0)));
        for (int i = 1; i < flds.size(); i++)
            sb.append(", " + listStringArrayToString(flds.get(i)));

        return sb.append("]").toString();
    }

    public String gridToString(List<List<Integer>> matrix) {
        if (matrix == null || matrix.size() <= 0)
            return "[]";

        StringBuilder sb = new StringBuilder("[");
        sb.append(listIntArrayToString(matrix.get(0)));
        for (int i = 1; i < matrix.size(); i++) {
            sb.append(", " + listIntArrayToString(matrix.get(i)));
        }
        sb.append("]");

        return sb.toString();
   }
}
