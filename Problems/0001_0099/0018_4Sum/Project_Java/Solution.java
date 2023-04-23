import java.util.*;

public class Solution {
    Set<List<Integer>> ansSet = new HashSet<>();
    public List<List<Integer>> fourSum(int[] nums, int target) {
        // 4ms
        ansSet = new HashSet<>();
        Arrays.sort(nums);
        df(nums, 0, nums.length - 1, target, 4, new ArrayList<Integer>());
        return new ArrayList<>(ansSet);
    }
    
    private void df(int[] nums, int l, int r, long target, long N, List<Integer> res) {
        if (r - l + 1 < N || N < 2 || target < nums[l]*N || target > nums[r]*N) {
            return;
        }
        if (N == 2) {
            while (l < r) {
                long s = (long)nums[l] + (long)nums[r];
                if (s == target) {
                    List<Integer> n_res = new ArrayList<>(res);
                    n_res.add(nums[l]);
                    n_res.add(nums[r]);
                    ansSet.add(n_res);
                    l++;
                    while (l < r && nums[l-1] == nums[l]) {
                        l++;
                    }
                } else if (s < target) {
                    l++;
                } else {
                    r--;
                }
            }
        } else {
            for (int i = l; i < r + 1; i++) {
                if (i == l || (i > l && nums[i-1] != nums[i])) {
                    List<Integer> temp = new ArrayList<>(res);
                    temp.add(nums[i]);
                    df(nums, i+1, r, target-(long)nums[i], N-1, temp);
                }
            }
        }
    }

    public List<List<Integer>> fourSum2(int[] nums, int target) {
        // 199ms - 201ms
        Arrays.sort(nums);
        Set<List<Integer>> ansSet = new HashSet<>();
        int n = nums.length;
        for (int i = 0; i <= n - 3; i++) {
            for (int j = i + 1; j <= n - 2; j++) {
                int k = j + 1;
                int l = n - 1;
                while (k < l) {
                    long sum = (long)nums[i] + nums[j] + nums[k] + nums[l];
                    if (sum == target) {
                        ansSet.add(List.of(nums[i], nums[j], nums[k], nums[l]));
                    }
                    if (sum >= target) {
                        l--;
                    } else {
                        k++;
                    }
                }
            }
        }
        return new ArrayList<>(ansSet);
    }

    public List<List<Integer>> fourSum_4for(int[] nums, int target) {
        // Time Limit Exceeded.
        int n = nums.length;
        if (n < 4)
            return new ArrayList<>();
        Arrays.sort(nums);
        Set<List<Integer>> ans = new HashSet<>();
        for (int i = 0; i < n; i++) 
            for (int j =  i + 1; j < n; j++) 
                for (int k =  j + 1; k < n; k++) 
                    for (int l = k + 1; l < n; l++) 
                        if (nums[i] + nums[j] + nums[k] + nums[l] == target) 
                            ans.add(Arrays.asList(nums[i], nums[j], nums[k], nums[l]));
        return new ArrayList(ans);
    }

    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds[0]);
        int target = Integer.parseInt(flds[1]);

        System.out.println("nums = " + ml.intArrayToString(nums));
        System.out.println("target = " + String.valueOf(target));

        long start = System.currentTimeMillis();
        
        List<List<Integer>> result = fourSum(nums, target);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
