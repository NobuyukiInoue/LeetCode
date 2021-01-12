import java.util.*;

public class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        // 10ms
        int canSkip = nums1.length - 0 + nums2.length - 0 - k;
        return helper(nums1, 0, nums2, 0, k, canSkip, 1).result;
    }

    public ResultInfo helper(int[] nums1, int start1, int[] nums2, int start2, int k, int canSkip, int ifSameThenWhich) {
        int[] result = new int[k];
        for (int index = 0; index < k; index++) {
            int max1Index = maxWithSkip(nums1, start1, canSkip);
            int max2Index = maxWithSkip(nums2, start2, canSkip);
            if (max1Index != -1 && max2Index != -1 && nums1[max1Index] > nums2[max2Index] || max1Index != -1 && max2Index == -1) {//第一个数组的大，选第一个数组
                result[index] = nums1[max1Index];
                canSkip = canSkip - (max1Index - start1);
                start1 = max1Index + 1;
            } else if (max1Index != -1 && max2Index != -1 && nums2[max2Index] > nums1[max1Index] || max2Index != -1 && max1Index == -1) {//第二个数组的大，选第二个数组
                result[index] = nums2[max2Index];
                canSkip = canSkip - (max2Index - start2);
                start2 = max2Index + 1;
            } else {
                boolean done = false;
                int newK = k - index - 1;
                int newStart1 = max1Index + 1;
                int canSkip1 = canSkip - (max1Index - start1);
                int newStart2 = max2Index + 1;
                int canSkip2 = canSkip - (max2Index - start2);
                ResultInfo resultInfo1 = new ResultInfo(null, newStart1, start2, canSkip1);
                ResultInfo resultInfo2 = new ResultInfo(null, start1, newStart2, canSkip2);
                for (int tmpK = 1; tmpK <= newK; tmpK++) {
                    resultInfo1 = helper(nums1, resultInfo1.start1, nums2, resultInfo1.start2, 1, resultInfo1.canSkip, 1);
                    int result1 = resultInfo1.result[0];
                    resultInfo2 = helper(nums1, resultInfo2.start1, nums2, resultInfo2.start2, 1, resultInfo2.canSkip, 2);
                    int result2 = resultInfo2.result[0];
                    if (result1 > result2) {
                        result[index] = nums1[max1Index];
                        canSkip = canSkip - (max1Index - start1);
                        start1 = max1Index + 1;
                        done = true;
                        break;
                    } else if (result1 < result2) {
                        result[index] = nums2[max2Index];
                        canSkip = canSkip - (max2Index - start2);
                        start2 = max2Index + 1;
                        done = true;
                        break;
                    }
                }
                if (!done) {
                    if (ifSameThenWhich == 1) {
                        result[index] = nums1[max1Index];
                        canSkip = canSkip - (max1Index - start1);
                        start1 = max1Index + 1;
                    } else {
                        result[index] = nums2[max2Index];
                        canSkip = canSkip - (max2Index - start2);
                        start2 = max2Index + 1;
                    }
                }
            }
        }
        return new ResultInfo(result, start1, start2, canSkip);
    }

    public int maxWithSkip(int[] nums, int start, int canSkip) {
        if (start == nums.length) {
            return -1;
        }
        int index = start;
        for (int i = 1; i <= canSkip; i++) {
            if (start + i < nums.length && nums[start + i] > nums[index]) {
                index = start + i;
            }
        }
        return index;
    }

    class ResultInfo {
        int[] result;
        int start1;
        int start2;
        int canSkip;
    
        public ResultInfo(int[] result, int start1, int start2, int canSkip) {
            this.result = result;
            this.start1 = start1;
            this.start2 = start2;
            this.canSkip = canSkip;
        }
    }

    public int[] maxNumber_bad(int[] nums1, int[] nums2, int k) {
        int N1 = nums1.length;
        int N2 = nums2.length;
        List<Integer[]> next_candidates = new ArrayList<>();
        next_candidates.add(new Integer[] {0,0});
        int[] ret = new int[k];

        for (int remain = k; remain > 0; remain--) {
            List<Integer[]> candidates = next_candidates;
            next_candidates = new ArrayList<>();
            next_candidates.add(new Integer[] {0,0});
            int value_max = -1;
            for (Integer[] i : candidates) {
                if (i[0] >= N1 && i[1] >= N2) {
                    continue;
                }
                int r1 = N1 - i[0];
                int r2 = N2 - i[1];
                int max_skip = r1 + r2 - remain;
                int[] jv1 = getCandidate(nums1, i[0], max_skip);
                int[] jv2 = getCandidate(nums2, i[1], max_skip);
                if (jv1[1] > value_max) {
                    next_candidates = new ArrayList<>();
                    next_candidates.add(new Integer[] {jv1[0] + 1, i[1]});
                    value_max = jv1[1];
                } else if (jv1[0] == value_max) {
                    next_candidates.add(new Integer[] {jv1[0] + 1, i[1]});
                }
                if (jv2[1] > value_max) {
                    next_candidates = new ArrayList<>();
                    next_candidates.add(new Integer[] {i[0], jv2[0] + 1});
                    value_max = jv2[1];
                } else if (jv2[1] == value_max) {
                    next_candidates.add(new Integer[] {i[0], jv2[0] + 1});
                }
            }
            ret[ret.length - remain] = value_max;
        }
        return ret;
    }

    private int[] getCandidate(int[] nums, int start, int max_skip) {
        int[] res = new int[] {start, -1};
        for (int i = start; i < Math.min(nums.length, start + max_skip + 1); i++) {
            if (res[1] < nums[i]) {
                res[0] = i;
                res[1] = nums[res[0]];
                if (nums[res[0]] == 9) {
                    break;
                }
            }
        }
        return res;
    }


    public void Main(String temp) {
        String[] flds = temp.replace("\"", "").replace(" ", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        int k = Integer.parseInt(flds[2]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2) + ", k = " + Integer.toString(k));

        long start = System.currentTimeMillis();

        int[] result = maxNumber(nums1, nums2, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.intArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
