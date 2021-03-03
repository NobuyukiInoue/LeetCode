import java.util.*;

public class Solution {
    public boolean isPossible(int[] nums) {
        // 3ms
        int n = nums.length;
        if (n < 3)
            return false;

        int first = nums[0];
        int last = nums[n-1];

        int start = Math.abs(first);
        int arr[] = new int[start + last + 2];

        for(int num:nums)
            arr[start + num]++;

        if (last - first < 2)
            return false;

        while (first <= last) {
            int count = 0;   
            for (int i = first; i <= last; i++) {
                if (arr[i + start] == 0) {
                    if (count < 3) {
                        return false;
                    } else {
                        break;
                    }
                }
                if(count >= 3 && arr[i - 1 + start] >= arr[i + start]) {
                        break;
                }
                arr[i + start]--;
                count++;
            }

            if(count < 3) {
                return false;
            }

            while(arr[first + start] == 0 && first <= last) {
                first++;
            }
        }
        return true;
    }

    public boolean isPossible2(int[] nums) {
        // 22ms
        HashMap<Integer, Integer> left = new HashMap<>();

        for (int num : nums) {
            left.put(num, left.getOrDefault(num, 0) + 1);
        }

        HashMap<Integer, Integer> right = new HashMap<>();
        for (int i : nums) {
            if (left.get(i) == 0) {
                continue;
            }
            left.put(i, left.getOrDefault(i, 0) - 1);
            if (right.getOrDefault(i - 1, 0) > 0) {
                right.put(i - 1, right.getOrDefault(i - 1, 0) - 1);
                right.put(i, right.getOrDefault(i, 0) + 1);
            } else if (left.getOrDefault(i + 1, 0) > 0 && left.getOrDefault(i + 2, 0) > 0) {
                left.put(i + 1, left.get(i + 1) - 1);
                left.put(i + 2, left.get(i + 2) - 1);
                right.put(i + 2, right.getOrDefault(i + 2, 0) + 1);
            } else {
                return false;
            }
        }
        return true;
    }

    public void Main(String temp) {
        String flds = temp.replace("[", "").replace("]", "").replace(", ", ",").trim();

        Mylib ml = new Mylib();
        int[] nums = ml.stringToIntArray(flds);
        System.out.println("nums = " + ml.intArrayToString(nums));

        long start = System.currentTimeMillis();

        boolean result = isPossible(nums);

        long end = System.currentTimeMillis();

        System.out.println("result = " + Boolean.toString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
