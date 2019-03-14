import java.util.*;

public class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
         // map from x to next greater element of x
        Map<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        for (int num : nums2) {
            while (!stack.isEmpty() && stack.peek() < num)
                map.put(stack.pop(), num);
            stack.push(num);
        }   
        for (int i = 0; i < nums1.length; i++)
            nums1[i] = map.getOrDefault(nums1[i], -1);
        return nums1;
    }

    public void Main(String args) {
        System.out.println("args = " + args);
        String[] flds = args.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.str_to_int_array(flds[0]);
        int[] nums2 = ml.str_to_int_array(flds[1]);

        System.out.println("nums1 = " + ml.output_int_array(nums1));
        System.out.println("nums2 = " + ml.output_int_array(nums2));

        long start = System.currentTimeMillis();

        int[] result = nextGreaterElement(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = " +  ml.output_int_array(result));
        System.out.println((end - start)  + "ms\n");
    }
}
