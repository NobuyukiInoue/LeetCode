import java.util.*;

public class Solution {
    public int[] arrayRankTransform(int[] arr) {
        // 43ms
        int N = arr.length;
        int[] ranks = Arrays.copyOf(arr, N);
        Arrays.sort(ranks);
        int rank = 1;
        HashMap<Integer, Integer> m = new HashMap();
        for (int n : ranks) {
            if (!m.containsKey(n))
                m.put(n, rank++);
        }
        for (int i = 0; i < N; i++) 
            ranks[i] = m.get(arr[i]);
        return ranks;
    }

    public int[] decompressRLElist2(int[] nums) {
        // 3ms
		int len = 0;
        for (int i = 0; i < nums.length; i += 2)
            len += nums[i];
        int[] res = new int[len];
        int p = 0;
        for (int i = 0; i < nums.length; i += 2) {
			for (int j = 0; j < nums[i]; j++) {
                res[p++] = nums[i + 1];
            }
        }
        return res;
    }

    public String Int_array_to_String(int[] data) {
        String result = "";
    
        for (int i = 0; i < data.length; i++) {
            if (i > 0)
                result += ",";

            if (data[i] == -1)
                result += "null";
            else
                result += Integer.toString(data[i]);
        }
    
        return result;
    }

    public String List_array_to_String(List<Integer> list) {
        if (list.size() <= 0)
            return "[]";

        String resultStr = "[" + Integer.toString(list.get(0));
        for (Integer i = 1; i < list.size(); i++) {
            resultStr += "," + Integer.toString(list.get(i));
        }

        return resultStr + "]";
    }

    public void Main(String temp) {
        String flds = temp.replace("\"", "").replace(" ", "").replace("[", "").replace("]", "").trim();

        Mylib mc = new Mylib();
        int[] arr = mc.str_to_int_array(flds);
        System.out.println("arr = [" + Int_array_to_String(arr) + "]");

        long start = System.currentTimeMillis();
        
        int[] result = arrayRankTransform(arr);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Int_array_to_String(result));
        System.out.println((end - start)  + "ms\n");
    }
}
