import java.util.*;

public class Solution {
    public void calc(String[] cmds, String[] args) {
        Boolean createdKthLargest = false;

        String[] flds = args[0].replace("]", "").split(",\\[");
        int k = Integer.parseInt(flds[0]);
        int[] nums;

        if (flds.length < 2) {
            nums = null;
        } else {
            String[]nums_str = flds[1].split(",");

            if (nums_str.length == 0) {
                nums = null;
            } else {
                nums = new int[nums_str.length];

                for (int i = 0; i < nums.length; i++) {
                    nums[i] = Integer.parseInt(nums_str[i]);
                }
            }
        }

        KthLargest Kth = new KthLargest(k, nums);
        createdKthLargest = true;

        for (int i = 0; i < cmds.length; i++ ) {
            if (createdKthLargest != true) {
                System.out.println("KthLargest() is not executed.");
                System.exit(1);
            } else if (cmds[i].equals("add")) {
                int result = Kth.add(Integer.parseInt(args[i]));
                System.out.println("Execute add(" + Integer.parseInt(args[i]) + ") = " + Integer.toString(result));
            }
        }
    }

    public String StringArray2String(String[] data) {
        if (data.length <= 0)
            return "";

        String resultStr;
        if (data[0].length() == 0) {
            resultStr = "null";
        } else {
            resultStr = data[0];
        }

        for (int i = 1; i < data.length; i++) {
            if (data[i].length() == 0) {
                resultStr += ", null";
            } else {
                resultStr += ", " + data[i];
            }

        }

        return resultStr;
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("]]]", "").trim().split("\\],\\[\\[");
        String[] cmds = flds[0].replace("[[", "").split(",");
        String[] args = flds[1].split("\\],\\[");

        System.out.println("cmds[] = " + StringArray2String(cmds));
        System.out.println("args[] = " + StringArray2String(args));

        long start = System.currentTimeMillis();
        
        calc(cmds, args);

        long end = System.currentTimeMillis();

        System.out.println((end - start)  + "ms\n");
    }
}
