import java.util.*;

public class Solution {
    // 3ms

    class IntegerWrapper implements Comparable<IntegerWrapper> {
        int row;
        int colunm;
        int value;
    
        public IntegerWrapper(int row, int colunm, int value) {
            this.row = row;
            this.colunm = colunm;
            this.value = value;
        }
    
        @Override
        public int compareTo(IntegerWrapper o) {
            return Integer.compare(this.value, o.value);
        }
    }

    public List<List<Integer>> kSmallestPairs(int[] nums1, int[] nums2, int k) {
        List<List<Integer>> answer = new ArrayList<List<Integer>>();
        if (nums1.length > 0 && nums2.length > 0) {
            int length = nums1.length;
            PriorityQueue<IntegerWrapper> heap = new PriorityQueue<>(length);
            for (int row = 0; row < length; row++) {
                heap.add(new IntegerWrapper(row, 0, nums1[row] + nums2[0]));
            }
            while (k > 0 && heap.size() > 0) {
                IntegerWrapper wrapper = heap.poll();
                List<Integer> temp = new ArrayList<Integer>();
                temp.add(nums1[wrapper.row]);
                temp.add(nums2[wrapper.colunm]);
                answer.add(temp);
                wrapper.colunm++;
                if (wrapper.colunm < nums2.length) {
                    wrapper.value = nums1[wrapper.row] + nums2[wrapper.colunm];
                    heap.add(wrapper);
                }
                k--;
            }
        }
        return answer;
    }

    public void Main(String temp) {
        String[] flds = temp.replace(" ", "").replace("\"", "").replace("\"", "").replace("[[", "").replace("]]", "").trim().split("\\],\\[");

        Mylib ml = new Mylib();
        int[] nums1 = ml.stringToIntArray(flds[0]);
        int[] nums2 = ml.stringToIntArray(flds[1]);
        int k = Integer.parseInt(flds[2]);
        System.out.println("nums1 = " + ml.intArrayToString(nums1) + ", nums2 = " + ml.intArrayToString(nums2) + ", k = " + k);

        long start = System.currentTimeMillis();

        List<List<Integer>> result = kSmallestPairs(nums1, nums2, k);

        long end = System.currentTimeMillis();

        System.out.println("result = " + ml.listListIntArrayToString(result));
        System.out.println((end - start)  + "ms\n");
    }
}
