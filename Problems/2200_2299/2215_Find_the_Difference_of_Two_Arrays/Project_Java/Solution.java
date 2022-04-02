import java.util.*;
import java.util.stream.*;

public class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        // 11ms - 23ms
        LinkedHashSet<Integer>s1 = new LinkedHashSet<>();
        LinkedHashSet<Integer>s2 = new LinkedHashSet<>();
        for (int num : nums1) {
            s1.add(num);
        }
        for (int num : nums2) {
            s2.add(num);
        }

        List<Integer>list1 = new ArrayList<>();
        List<Integer>list2 = new ArrayList<>();
        for(int num : s1) {
            if (!s2.contains(num)) {
                list1.add(num);
            }   
        }
        for (int num : s2) {
            if(!s1.contains(num)) {
                list2.add(num);
            }
        }

        List<List<Integer>> ans = new ArrayList<>();
        ans.add(list1);
        ans.add(list2);
        return ans;
    }

    public List<List<Integer>> findDifference_use_stream(int[] nums1, int[] nums2) {
        Set<Integer> s1 = Arrays.stream(nums1).boxed().collect(Collectors.toSet());
        Set<Integer> s2 = Arrays.stream(nums2).filter(n -> !s1.contains(n)).boxed().collect(Collectors.toSet());
        Arrays.stream(nums2).forEach(s1::remove);
        return Arrays.asList(new ArrayList<>(s1), new ArrayList<>(s2));
    }

    public void Main(String temp) {
        String flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim();
        String[] str_mat = flds.split("\\],\\[");

        Mylib ml = new Mylib();
        int[][] nums = ml.stringToIntIntArray(str_mat);
        int[] nums1 = nums[0], nums2 = nums[1];
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2));

        long start = System.currentTimeMillis();

        List<List<Integer>> result = findDifference(nums1, nums2);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
